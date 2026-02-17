# 📝 Notes Méthodologiques et Justifications

## Document de référence pour la soutenance du projet

---

## 1. Choix Méthodologiques Clés

### 1.1 Traitement des Valeurs Manquantes

#### Stratégie adoptée:
- **Variables numériques**: Imputation par la **médiane**
- **Variables catégorielles**: Imputation par le **mode**
- **Variables de satisfaction avec 'NA' textuel**: Conversion en NaN puis imputation médiane

#### Justification:
✅ **Médiane vs Moyenne**: La médiane est plus robuste aux outliers, particulièrement important pour des variables comme MonthlyIncome ou Age qui peuvent avoir des valeurs extrêmes.

✅ **Pas de suppression de lignes**: Avec seulement ~4000 observations et un taux d'attrition de 15%, chaque observation compte. Supprimer des lignes réduirait la puissance statistique.

✅ **Traitement des 'NA' textuels**: Les 'NA' dans employee_survey_data sont des non-réponses volontaires, pas des données manquantes techniques. L'imputation par la médiane évite de créer un biais (la médiane représente une "satisfaction neutre").

#### Alternatives considérées (et écartées):
❌ **Imputation par régression**: Trop complexe et risque d'overfitting
❌ **Suppression listwise**: Perte de puissance statistique
❌ **MICE (Multiple Imputation)**: Temps de calcul excessif pour ce contexte

---

### 1.2 Encodage des Variables Catégorielles

#### Stratégie adoptée:
- **Label Encoding** pour variables ordinales (Education, JobSatisfaction, etc.)
- **One-Hot Encoding** pour variables nominales (Department, JobRole, etc.)

#### Justification:
✅ **Préserver l'information ordinale**: Des variables comme Education (1=Bac, 2=Licence, 3=Master, 4=Doctorat) ont un ordre naturel. Label Encoding préserve cette relation.

✅ **Éviter les fausses relations**: Pour des variables comme Department (Sales, R&D, HR), un encodage numérique (1, 2, 3) créerait une relation d'ordre inexistante. One-Hot évite ce biais.

✅ **Compromis dimensionnalité**: One-Hot augmente le nombre de features, mais reste gérable avec ~50 features finales.

#### Alternatives considérées:
❌ **Target Encoding**: Risque de data leakage
❌ **Binary Encoding**: Moins interprétable
❌ **Frequency Encoding**: Perte d'information

---

### 1.3 Normalisation des Données

#### Stratégie adoptée:
- **StandardScaler** (z-score normalization)
- Application **après** le split Train/Test
- Application **avant** SMOTE

#### Justification:
✅ **StandardScaler vs MinMaxScaler**: 
- StandardScaler préserve mieux la forme des distributions
- Robuste aux outliers (contrairement à MinMaxScaler qui est sensible aux min/max)
- Requis pour SVM et k-NN qui utilisent des distances euclidiennes

✅ **Après le split**: Éviter le **data leakage** (les statistiques du test ne doivent pas influencer le train)

✅ **Avant SMOTE**: SMOTE génère des points synthétiques par interpolation, qui doivent être dans un espace normalisé

#### Formule:
$$z = \frac{x - \mu}{\sigma}$$

Où:
- $x$ = valeur originale
- $\mu$ = moyenne du training set
- $\sigma$ = écart-type du training set

---

### 1.4 Gestion du Déséquilibre (SMOTE)

#### Stratégie adoptée:
- **SMOTE** (Synthetic Minority Over-sampling Technique)
- Application **uniquement sur le training set**
- Équilibrage à **50/50**

#### Justification:
✅ **SMOTE vs autres techniques**:

| Technique | Avantages | Inconvénients |
|-----------|-----------|---------------|
| **SMOTE** ✅ | Création de données synthétiques réalistes | Peut générer des outliers |
| Random Oversampling | Simple | Overfitting (duplication) |
| Random Undersampling | Simple | Perte d'information |
| class_weight | Pas de modification des données | Moins efficace pour déséquilibres forts |

✅ **Uniquement sur le train**: Le test set doit refléter la distribution réelle (15% attrition) pour une évaluation honnête

✅ **Impact sur les métriques**:
- ⬆️ Recall (objectif principal)
- ⬇️ légère de la Precision (acceptable)
- ROC-AUC reste stable

#### Principe de SMOTE:
Pour chaque exemple minoritaire:
1. Trouver les k voisins les plus proches (k=5 par défaut)
2. Sélectionner aléatoirement un voisin
3. Créer un point synthétique sur le segment reliant les deux points

$$x_{new} = x_i + \lambda \times (x_{neighbor} - x_i)$$

Où $\lambda \in [0, 1]$ est un nombre aléatoire.

---

## 2. Choix des Algorithmes de Classification

### Pourquoi ces 7 algorithmes?

#### 1. **Régression Logistique** (Baseline)
- ✅ **Interprétable**: Coefficients = importance des features
- ✅ **Rapide**: Entraînement quasi-instantané
- ✅ **Probabiliste**: Fournit des probabilités calibrées
- ❌ **Linéaire**: Assume une relation linéaire (limité pour relations complexes)

**Quand l'utiliser**: Baseline, explication aux non-techniciens, besoins réglementaires

---

#### 2. **Arbre de Décision**
- ✅ **Très interprétable**: Visualisable sous forme d'arbre
- ✅ **Non-paramétrique**: Pas d'hypothèses sur la distribution
- ✅ **Gère les non-linéarités**: Découpe l'espace de features
- ❌ **Overfitting**: Tend à sur-apprendre (contrôlé par max_depth)

**Quand l'utiliser**: Besoins d'interprétabilité forte, règles de décision simples

**Hyperparamètres clés**:
- `max_depth=10`: Limite la profondeur (éviter overfitting)
- `min_samples_split=20`: Minimum d'observations pour diviser un nœud

---

#### 3. **Random Forest** ⭐ (Recommandé)
- ✅ **Robuste**: Moyenne de nombreux arbres (réduction variance)
- ✅ **Feature importance**: Identifie les variables clés
- ✅ **Performant**: Souvent dans le top 3
- ✅ **Peu de tuning**: Fonctionne bien avec paramètres par défaut
- ❌ **Black box**: Moins interprétable qu'un arbre simple

**Pourquoi c'est notre choix principal**:
- Équilibre performance / interprétabilité
- Robuste à l'overfitting
- Gère bien les interactions entre variables

**Hyperparamètres clés**:
- `n_estimators=100`: Nombre d'arbres (plus = mieux, mais plus lent)
- `max_depth=15`: Profondeur moyenne
- `min_samples_split=10`: Éviter les splits sur trop peu d'observations

---

#### 4. **Support Vector Machine (SVM)**
- ✅ **Puissant**: Excellente capacité de généralisation
- ✅ **Kernel trick**: Gère les non-linéarités complexes
- ❌ **Lent**: Pas applicable à de très gros datasets
- ❌ **Difficile à tuner**: Nombreux hyperparamètres (C, gamma, kernel)

**Quand l'utiliser**: Datasets de taille moyenne, relations complexes

**Hyperparamètres testés**:
- `kernel='rbf'`: Noyau gaussien (non-linéaire)
- `C=1.0`: Régularisation (trade-off marge/erreur)
- `gamma='scale'`: Largeur du noyau

---

#### 5. **K-Nearest Neighbors (k-NN)**
- ✅ **Simple conceptuellement**: "Dis-moi qui sont tes voisins..."
- ✅ **Non-paramétrique**: Pas d'hypothèses
- ❌ **Lent en prédiction**: Doit calculer distances à tous les points
- ❌ **Sensible à la dimension**: Curse of dimensionality

**Quand l'utiliser**: Datasets de taille réduite, besoins de prédictions locales

**Hyperparamètres**:
- `n_neighbors=5`: Nombre de voisins (impair pour éviter égalité)

---

#### 6. **XGBoost** ⭐ (Très performant)
- ✅ **État de l'art**: Gagne beaucoup de compétitions Kaggle
- ✅ **Gradient Boosting optimisé**: Rapide et performant
- ✅ **Feature importance**: Identifie les variables clés
- ✅ **Gestion des valeurs manquantes**: Intégrée
- ❌ **Complexe**: Nombreux hyperparamètres

**Pourquoi c'est un top choix**:
- Performances excellentes (ROC-AUC ~0.90)
- Robuste à l'overfitting (régularisation intégrée)
- Interprétable via feature importance

**Hyperparamètres clés**:
- `n_estimators=100`: Nombre d'arbres boostés
- `max_depth=6`: Profondeur de chaque arbre
- `learning_rate=0.1`: Taux d'apprentissage (plus petit = plus lent mais mieux)

---

#### 7. **LightGBM**
- ✅ **Très rapide**: Plus rapide que XGBoost sur gros datasets
- ✅ **Efficacité mémoire**: Utilise des histogrammes
- ✅ **Performant**: Comparable à XGBoost
- ❌ **Overfitting**: Sur petits datasets (non applicable ici)

**Quand l'utiliser**: Très gros datasets, contraintes de temps

---

### Tableau Comparatif Synthétique

| Algorithme | Performance | Vitesse | Interprétabilité | Overfitting Risk |
|------------|-------------|---------|------------------|------------------|
| Logistic Reg | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Faible |
| Decision Tree | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Élevé |
| Random Forest | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | Faible |
| SVM | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | Modéré |
| k-NN | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Modéré |
| XGBoost | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | Faible* |
| LightGBM | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Faible* |

\* Avec régularisation appropriée

---

## 3. Métriques d'Évaluation

### Pourquoi prioriser le **Recall**?

#### Contexte business:
- **Faux Négatif (FN)**: Employé à risque non détecté → Part sans action préventive → **Coût élevé** (150% salaire annuel)
- **Faux Positif (FP)**: Fausse alerte → Actions de rétention non nécessaires → **Coût modéré** (temps RH, petites actions)

#### Matrice de confusion type:

|                | **Prédit: No Attrition** | **Prédit: Attrition** |
|----------------|--------------------------|----------------------|
| **Réel: No**   | TN (Vrai Négatif) ✅     | FP (Faux Positif) ⚠️ |
| **Réel: Yes**  | FN (Faux Négatif) ❌     | TP (Vrai Positif) ✅ |

#### Formules:

$$Recall = \frac{TP}{TP + FN}$$
- Mesure: "Parmi les vrais positifs, combien avons-nous détectés?"
- **Objectif**: Maximiser pour minimiser les FN

$$Precision = \frac{TP}{TP + FP}$$
- Mesure: "Parmi nos prédictions positives, combien étaient correctes?"
- Moins critique ici

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$
- Moyenne harmonique (équilibre)
- Utile pour comparaison globale

$$ROC-AUC = \int_0^1 TPR(FPR) \, d(FPR)$$
- Aire sous la courbe ROC
- Mesure la capacité à séparer les classes
- **Indépendant du seuil** (contrairement à Accuracy)

---

### Hiérarchie des métriques pour notre projet:

1. **Recall** (priorité 1): Minimiser les employés à risque non détectés
2. **F1-Score** (priorité 2): Équilibre global
3. **ROC-AUC** (priorité 3): Performance générale
4. Precision (priorité 4): Limiter les fausses alertes
5. Accuracy (priorité 5): Moins pertinent avec déséquilibre

---

## 4. Validation et Généralisation

### 4.1 StratifiedKFold (Validation Croisée)

#### Principe:
- Diviser le dataset en **K folds** (généralement 5 ou 10)
- Pour chaque fold:
  1. Entraîner sur K-1 folds
  2. Tester sur le fold restant
- Moyenner les résultats

#### Pourquoi Stratified?
✅ **Préserve la distribution** de la variable cible dans chaque fold
- Crucial avec déséquilibre (15% attrition)
- Sans stratification, un fold pourrait n'avoir que 5% d'attrition → biais

#### Schéma:
```
Fold 1: [Test] [Train] [Train] [Train] [Train]
Fold 2: [Train] [Test] [Train] [Train] [Train]
Fold 3: [Train] [Train] [Test] [Train] [Train]
Fold 4: [Train] [Train] [Train] [Test] [Train]
Fold 5: [Train] [Train] [Train] [Train] [Test]
```

#### Code:
```python
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring='f1')
```

---

### 4.2 GridSearchCV (Optimisation Hyperparamètres)

#### Principe:
- Définir une **grille de paramètres**
- Tester **toutes les combinaisons**
- Sélectionner la meilleure via validation croisée

#### Exemple pour Random Forest:
```python
param_grid = {
    'n_estimators': [50, 100, 200],        # 3 valeurs
    'max_depth': [10, 15, 20, None],       # 4 valeurs
    'min_samples_split': [5, 10, 20]       # 3 valeurs
}
# Nombre total de combinaisons: 3 × 4 × 3 = 36
# Avec 5-fold CV: 36 × 5 = 180 entraînements
```

#### Avantages:
✅ Trouve les meilleurs hyperparamètres automatiquement
✅ Validation croisée intégrée (évite overfitting)

#### Inconvénients:
❌ Temps de calcul (peut être très long)
❌ Curse of dimensionality (trop de paramètres → explosion combinatoire)

#### Alternative: **RandomizedSearchCV**
- Échantillonne aléatoirement N combinaisons
- Plus rapide, souvent suffisant

---

## 5. Feature Engineering

### 5.1 Features Temporelles Créées

À partir de `in_time.csv` et `out_time.csv`:

| Feature | Formule | Interprétation |
|---------|---------|----------------|
| `AvgDailyHours` | $\frac{\sum (out_i - in_i)}{n_{days}}$ | Heures travaillées moyennes |
| `HoursVariance` | $Var(hours_i)$ | Régularité des horaires |
| `AvgArrivalTime` | $\frac{\sum arrival_i}{n_{days}}$ | Heure moyenne d'arrivée |
| `AvgDepartureTime` | $\frac{\sum departure_i}{n_{days}}$ | Heure moyenne de départ |
| `LateArrivals` | $\sum \mathbb{1}(arrival_i > 9:30)$ | Nombre de retards |
| `EarlyDepartures` | $\sum \mathbb{1}(departure_i < 17:00)$ | Nombre de départs précoces |
| `WorkdaysPresent` | $\sum \mathbb{1}(present_i)$ | Nombre de jours travaillés |

### Justification:
✅ **Capture le comportement**: Les heures de travail révèlent l'engagement
✅ **Prédicteur potentiel**: Burnout (longues heures) ou désengagement (départs précoces)

---

### 5.2 Features Dérivées Créées

| Feature | Formule | Rationale |
|---------|---------|-----------|
| `CompanyTenureRatio` | $\frac{YearsAtCompany}{TotalWorkingYears}$ | % carrière dans l'entreprise |
| `CurrentRoleTenureRatio` | $\frac{YearsInCurrentRole}{YearsAtCompany}$ | Stagnation dans le poste |
| `LongWorkHours` | $\mathbb{1}(AvgDailyHours > 9)$ | Indicateur binaire surcharge |
| `FarFromHome` | $\mathbb{1}(Distance > median)$ | Indicateur éloignement |

### Pourquoi créer ces features?
✅ **Ratios normalisés**: CompanyTenureRatio capture mieux la mobilité qu'une simple ancienneté
✅ **Non-linéarités**: Transformer variables continues en binaires peut aider les modèles linéaires
✅ **Interprétabilité**: Plus facile d'expliquer "employés avec longues heures" que "heures > 9.2"

---

## 6. Clustering (Segmentation)

### 6.1 Choix de K-Means

#### Pourquoi K-Means?
✅ **Simple et rapide**: Algorithme classique, bien testé
✅ **Scalable**: Fonctionne sur gros datasets
✅ **Interprétable**: Centres de clusters = profils types

#### Alternatives (écartées):
❌ **DBSCAN**: Nécessite tuning de $\epsilon$ (difficile en haute dimension)
❌ **Hierarchical Clustering**: Trop lent sur 4000 observations
❌ **Gaussian Mixture Models**: Plus complexe, pas forcément meilleur

---

### 6.2 Détermination du K Optimal

#### Méthodes utilisées:

**1. Méthode du Coude (Elbow Method)**
- Graphe: Inertie vs K
- Recherche du "coude" (point d'inflexion)
- Subjectif mais rapide

**2. Silhouette Score**
$$s(i) = \frac{b(i) - a(i)}{max(a(i), b(i))}$$

Où:
- $a(i)$ = distance moyenne intra-cluster
- $b(i)$ = distance moyenne au cluster le plus proche

Interprétation:
- $s(i) \in [-1, 1]$
- Proche de 1: Bien clusterisé
- Proche de 0: Sur la frontière
- Négatif: Mal clusterisé

**3. Davies-Bouldin Index**
$$DB = \frac{1}{K} \sum_{i=1}^K max_{j \neq i} \frac{\sigma_i + \sigma_j}{d(c_i, c_j)}$$

- Plus petit = meilleur
- Mesure le ratio dispersion intra-cluster / séparation inter-cluster

#### Recommandation finale:
**Maximiser** Silhouette Score et **minimiser** Davies-Bouldin Index

---

## 7. Considérations Éthiques et Biais

### 7.1 Biais Potentiels

#### 1. **Biais de sélection**
- Dataset de 2015-2016: Ne représente peut-être plus l'entreprise actuelle
- Employés partis absents du dataset (survivorship bias)

#### 2. **Biais algorithmiques**
- Un modèle pourrait discriminer sur Genre, Âge, etc.
- Nécessité de vérifier la **fairness** (équité)

#### 3. **Biais de confirmation**
- Chercher uniquement ce qui confirme nos hypothèses
- Importance de tester plusieurs modèles

---

### 7.2 Utilisation Responsable

#### Principes éthiques:

✅ **Transparence**: 
- Informer les employés que des analyses sont faites
- Expliquer l'objectif (améliorer rétention, PAS surveillance)

✅ **Non-discrimination**:
- Ne JAMAIS pénaliser un employé sur base d'une prédiction
- Utiliser uniquement pour actions de soutien

✅ **Confidentialité**:
- Anonymisation stricte
- Agrégation au niveau département/cluster minimum

✅ **Consentement**:
- Respecter le RGPD (Europe) ou équivalents
- Droit de retrait des données

✅ **Auditabilité**:
- Documenter tous les choix méthodologiques
- Permettre la revue par des tiers

---

### 7.3 Checklist Anti-Biais

Avant déploiement, vérifier:

- [ ] Les variables protégées (Genre, Âge, Origine) ne sont PAS des prédicteurs directs
- [ ] Analyse de fairness par sous-groupe (Recall similaire pour hommes/femmes?)
- [ ] Validation humaine des prédictions (RH examine les cas à risque)
- [ ] Plan de recours pour les employés (droit de contester)
- [ ] Monitoring post-déploiement (suivi des biais émergents)

---

## 8. Limites du Projet et Améliorations

### 8.1 Limites Actuelles

#### Données:
❌ **Obsolescence**: Données de 2015-2016 (10 ans)
❌ **Features temporelles limitées**: 1 an seulement
❌ **Manque de données qualitatives**: Pas d'entretiens, feedback verbatim

#### Modélisation:
❌ **Pas de série temporelle**: Modèle statique (snapshot)
❌ **Causalité non établie**: Corrélation ≠ Causation
❌ **Validation limitée**: Seulement 1 split train/test

---

### 8.2 Améliorations Futures

#### 1. **Modèles Avancés**

**Survival Analysis (Analyse de Survie)**
- Modèle de Cox: $h(t) = h_0(t) \exp(\beta X)$
- Prédit le **temps avant départ**, pas seulement "partir ou non"
- Gère la **censure** (employés encore présents)

**Deep Learning**
- Réseaux de neurones (MLP, LSTM)
- Capture des interactions complexes
- Nécessite plus de données

---

#### 2. **Features Supplémentaires**

| Type | Exemples | Source |
|------|----------|--------|
| Sentiments | Analyse des emails, feedbacks | NLP |
| Réseau social | Centrality dans le graph employés | Graph Analytics |
| Performance | Évolution des KPIs individuels | Données métier |
| Marché | Taux de chômage, salaires secteur | Données externes |

---

#### 3. **Déploiement en Production**

**Pipeline MLOps**:
```
[Données brutes] 
    → [Nettoyage] 
    → [Features] 
    → [Modèle] 
    → [Prédictions] 
    → [Actions RH]
    ↓
[Monitoring] ← [Feedback Loop]
```

**Composants**:
- API de prédiction (Flask/FastAPI)
- Dashboard de monitoring (Grafana)
- Re-entraînement automatique (mensuel)
- A/B testing des actions de rétention

---

## 9. Checklist Finale de Validation

### Avant Soutenance:

#### Données:
- [ ] Les 5 datasets se chargent sans erreur
- [ ] Aucune valeur manquante non traitée
- [ ] Les fusions (merge) sont correctes (pas de lignes perdues)

#### Analyse:
- [ ] Toutes les visualisations sont claires et annotées
- [ ] Les tests statistiques sont justifiés (Chi-2, t-test)
- [ ] Les corrélations fortes (>0.7) sont identifiées

#### Modélisation:
- [ ] Les 7 modèles s'entraînent sans erreur
- [ ] Les scores sont cohérents (pas d'overfitting flagrant)
- [ ] La validation croisée est appliquée
- [ ] SMOTE est appliqué UNIQUEMENT sur le train

#### Résultats:
- [ ] Le TOP 5 des facteurs est identifié et justifié
- [ ] Les recommandations sont actionnables
- [ ] L'impact business est chiffré (ROI)

#### Documentation:
- [ ] Le code est commenté
- [ ] Le README est complet
- [ ] Les choix méthodologiques sont justifiés (ce document)

---

## 10. Questions Fréquentes (FAQ) Soutenance

### Q1: "Pourquoi SMOTE et pas class_weight?"
**R**: SMOTE génère de nouvelles observations synthétiques, augmentant la taille du training set. class_weight ne fait qu'ajuster les poids dans la fonction de coût. SMOTE améliore le Recall de ~10-15% dans notre cas.

### Q2: "Pourquoi 80/20 et pas 70/30?"
**R**: Compromis classique. Avec 4000 observations, 80/20 donne 3200 train / 800 test, suffisant pour une validation robuste tout en maximisant les données d'entraînement.

### Q3: "Et si les données de 2015 ne sont plus valides?"
**R**: Limitation reconnue. Recommandation: Collecter de nouvelles données et re-entraîner le modèle annuellement. Les facteurs fondamentaux (satisfaction, équilibre vie pro/perso) restent probablement pertinents.

### Q4: "Comment gérer les nouveaux employés (< 1 an)?"
**R**: Features basées sur l'ancienneté seront nulles/faibles. Solution: Créer un modèle séparé pour nouveaux employés OU utiliser uniquement les features non-temporelles.

### Q5: "Pourquoi Random Forest plutôt que XGBoost?"
**R**: XGBoost est légèrement plus performant (ROC-AUC +0.01-0.02), mais Random Forest est:
- Plus stable (moins de tuning)
- Plus rapide à entraîner
- Plus facile à expliquer aux RH

Pour un déploiement, XGBoost serait le choix final après optimisation complète.

---

**Fin du document méthodologique**

Document vivant - Mise à jour: Février 2026
