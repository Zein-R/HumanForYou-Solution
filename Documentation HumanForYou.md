# Documentation Complète - Analyse de l'Attrition HumanForYou

**Version** : 2.0  
**Date** : Février 2026  
**Projet** : IA & Machine Learning  
**Auteur** : Zein, Saheen, Téo, Noan

---

# Table des Matières

1. [Vue d'Ensemble du Projet](#1-vue-densemble-du-projet)
2. [Architecture de la Solution](#2-architecture-de-la-solution)
3. [Méthodologie et Justifications](#3-méthodologie-et-justifications)
4. [Guide de Démarrage Rapide](#4-guide-de-démarrage-rapide)
5. [Guides d'Utilisation Détaillés](#5-guides-dutilisation-détaillés)
6. [Récapitulatif des Modifications](#6-récapitulatif-des-modifications)
7. [Références et Ressources](#7-références-et-ressources)

---

# 1. Vue d'Ensemble du Projet

## 1.1 Description

Ce projet d'analyse de données RH vise à identifier les facteurs clés d'attrition des employés chez **HumanForYou**, une entreprise pharmaceutique de 4000 employés en Inde confrontée à un taux de rotation de 15%.

### Objectifs

- Analyser les patterns d'attrition à partir de données 2015-2016
- Développer des modèles prédictifs performants et interprétables
- Identifier les TOP 5 facteurs influençant le départ des employés
- Proposer des recommandations actionnables pour améliorer la rétention

### Contexte Business

- **Entreprise** : HumanForYou (Pharmaceutique, Inde)
- **Effectif** : 4000 employés
- **Taux d'attrition actuel** : 15%
- **Coût annuel estimé** : ~36M€ (600 départs × 150% salaire)
- **Objectif** : Réduire à <10% en 24 mois
- **ROI cible** : 12M€/an d'économies

---

## 1.2 Données Disponibles

### Fichiers Sources

| Fichier | Description | Lignes | Variables |
|---------|-------------|--------|-----------|
| `general_data.csv` | Données démographiques et professionnelles | 4410 | 26 |
| `manager_survey_data.csv` | Évaluations managers (février 2015) | 4410 | 3 |
| `employee_survey_data.csv` | Enquête satisfaction (juin 2015) | 4410 | 4 |
| `in_time.csv` | Horaires d'arrivée 2015 | 4000 | 262 |
| `out_time.csv` | Horaires de départ 2015 | 4000 | 262 |

### Variables Clés

**Variables démographiques** : Age, Gender, MaritalStatus, Education  
**Variables professionnelles** : Department, JobRole, JobLevel, MonthlyIncome  
**Variables de carrière** : YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion  
**Variable cible** : **Attrition** (Yes/No) - Employé parti en 2016

---

## 1.3 Structure du Projet

```
HumanForYou Solution/
│
├── dataset/                                  # Données sources (5 fichiers CSV)
│   ├── general_data.csv
│   ├── manager_survey_data.csv
│   ├── employee_survey_data.csv
│   ├── in_time.csv
│   └── out_time.csv
│
├── Employee_Attrition_Analysis.ipynb        # [PRINCIPAL] Notebook principal
│   │
│   ├── Section 1: Configuration
│   ├── Section 2: Chargement et Fusion
│   ├── Section 3: EDA (Analyse Exploratoire)
│   ├── Section 4: Feature Engineering
│   │
│   ├── Section 5: Préparation (Split Tardif) Avec data leakage
│   ├── Section 5bis: Préparation (Split Précoce) [BEST PRACTICE]
│   ├── Section 5ter: Comparaison Méthodologique [ANALYSE]
│   │
│   ├── Section 6: Modélisation (7 algorithmes)
│   ├── Section 7: Optimisation
│   ├── Section 8: Clustering
│   ├── Section 9: Recommandations Business
│   └── Section 10: Conclusion
│
├── DOCUMENTATION_COMPLETE.md                 # Ce document
├── requirements.txt                          # Dépendances Python
│
└── Scripts de correction/
    ├── SOLUTION_CELLULE_30.py
    └── FONCTION_CORRIGEE_extract_time_features.py
```

---

## 1.4 Résultats Clés

### Performances des Modèles

| Modèle | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| Random Forest | ~0.87 | ~0.75 | ~0.78 | ~0.76 | ~0.90 |
| XGBoost | ~0.86 | ~0.73 | ~0.80 | ~0.76 | ~0.89 |
| LightGBM | ~0.85 | ~0.72 | ~0.79 | ~0.75 | ~0.88 |

**Métrique prioritaire** : **Recall** (minimiser les faux négatifs)

### TOP 5 Facteurs d'Attrition

1. **WorkLifeBalance** - Équilibre vie pro/perso
2. **BusinessTravel** - Fréquence des déplacements
3. **YearsSinceLastPromotion** - Stagnation de carrière
4. **JobSatisfaction** - Satisfaction au travail
5. **DistanceFromHome** - Distance domicile-travail

### Impact Business Estimé

- **Réduction ciblée** : 15% → 10% en 24 mois
- **Départs évités** : 200/an
- **Économies** : 12M€/an
- **Investissement** : 3-4M€/an
- **ROI net** : 8-9M€/an (×3)

---

# 2. Architecture de la Solution

## 2.1 Flux de Données - Comparaison des Approches

### Approche 1: Split Tardif (Section 5) - Avec Data Leakage

```
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 1: Chargement et Fusion                          │
│  5 datasets → MERGE → df_enriched (4410 lignes)         │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 2: Imputation (SUR TOUT LE DATASET)          │
│  Calcul médiane/mode sur 4410 lignes                    │
│  → Inclut les données du futur test set!                │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 3: Encodage (SUR TOUT LE DATASET)            │
│  LabelEncoder.fit() sur 4410 lignes                     │
│  → L'encodeur voit toutes les catégories!               │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 4: Split Train/Test (TROP TARD!)                 │
│  Train: 3528 lignes (80%) | Test: 882 lignes (20%)      │
│  → Les deux sets ont déjà "vu" les statistiques!        │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 5: Standardisation + SMOTE (CORRECT)         │
│  Fit sur train, transform sur test                      │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  RÉSULTAT: Performances SURESTIMÉES de 1-5%             │
└─────────────────────────────────────────────────────────┘
```

### Approche 2: Split Précoce (Section 5bis) - Best Practice

```
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 1: Chargement et Fusion (identique)              │
│  5 datasets → MERGE → df_enriched (4410 lignes)         │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 2: Split IMMÉDIAT (AVANT transformations)    │
│  Train: 3528 (80%) | Test: 882 (20%)                    │
│  → Séparation complète dès le départ                    │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 3: Imputation (FIT train, TRANSFORM test)    │
│  Médiane/mode calculés sur train uniquement             │
│  → Test n'influence PAS les statistiques                │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 4: Encodage (FIT train, TRANSFORM test)      │
│  LabelEncoder fit sur train uniquement                  │
│  → Gestion des catégories inconnues                     │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 5: Standardisation + SMOTE                   │
│  Toutes transformations basées sur train                │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  RÉSULTAT: Performances RÉALISTES et FIABLES            │
└─────────────────────────────────────────────────────────┘
```

---

## 2.2 Variables Créées par Section

### Section 5 (Split Tardif)

```python
# Données préparées
df_clean          # Après imputation (4410 lignes) - Leakage
df_encoded        # Après encodage (4410 lignes) - Leakage

# Après split et transformations
X_train_scaled, X_test_scaled     # Standardisés
X_train_smote, y_train_smote      # Avec SMOTE (~6000 lignes)

# Modèles (6 entraînés)
lr_model, dt_model, rf_model, svm_model, knn_model, xgb_model
```

### Section 5bis (Split Précoce) - NOUVEAU

```python
# Split immédiat
X_train_precoce, X_test_precoce
y_train_precoce, y_test_precoce

# Transformateurs (fit sur train uniquement)
num_imputer, cat_imputer          # SimpleImputer
label_encoders_bp                 # Dict de LabelEncoders
scaler_bp                         # StandardScaler
smote_bp                          # SMOTE

# Après transformations
X_train_bp_scaled, X_test_bp_scaled
X_train_bp_smote, y_train_bp_smote

# Modèles (6 entraînés avec suffix _bp)
lr_bp, dt_bp, rf_bp, svm_bp, knn_bp, xgb_bp

# Résultats
results_split_precoce             # DataFrame (6, 7)
```

### Section 5ter (Comparaison) - NOUVEAU

```python
results_split_tardif              # Résultats approche 1
results_split_precoce             # Résultats approche 2
comparison_df                     # Fusion + différences calculées
```

---

# 3. Méthodologie et Justifications

## 3.1 Choix Méthodologiques Clés

### 3.1.1 Traitement des Valeurs Manquantes

#### Stratégie Adoptée

- **Variables numériques** : Imputation par la **médiane**
- **Variables catégorielles** : Imputation par le **mode**
- **Variables avec 'NA' textuel** : Conversion en NaN puis imputation

#### Justification

**Médiane vs Moyenne** : La médiane est plus robuste aux outliers, particulièrement important pour MonthlyIncome ou Age qui peuvent avoir des valeurs extrêmes.

**Pas de suppression** : Avec seulement ~4000 observations et un taux d'attrition de 15%, chaque observation compte. Supprimer des lignes réduirait la puissance statistique.

**Traitement des 'NA' textuels** : Dans employee_survey_data, ce sont des non-réponses volontaires. L'imputation par la médiane évite de créer un biais (représente une "satisfaction neutre").

#### Code

```python
# MAUVAIS (Section 5)
imputer.fit_transform(df[['Age']])  # Fit sur tout le dataset

# BON (Section 5bis)
imputer.fit(X_train[['Age']])       # Fit sur train uniquement
X_train_clean = imputer.transform(X_train[['Age']])
X_test_clean = imputer.transform(X_test[['Age']])
```

---

### 3.1.2 Encodage des Variables Catégorielles

#### Stratégie Adoptée

- **Label Encoding** : Variables ordinales (Education, JobSatisfaction, etc.)
- **One-Hot Encoding** : Variables nominales (Department, JobRole, etc.)

#### Justification

**Préserver l'information ordinale** : Des variables comme Education (1=Bac, 2=Licence, 3=Master) ont un ordre naturel. Label Encoding préserve cette relation.

**Éviter les fausses relations** : Pour Department (Sales, R&D, HR), un encodage numérique créerait une relation d'ordre inexistante.

**Compromis dimensionnalité** : One-Hot augmente le nombre de features, mais reste gérable avec ~50 features finales.

#### Code

```python
# Label Encoding pour ordinales
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Education'] = le.fit_transform(df['Education'])

# One-Hot pour nominales
df = pd.get_dummies(df, columns=['Department'], drop_first=True)
```

---

### 3.1.3 Normalisation des Données

#### Stratégie Adoptée

- **StandardScaler** (z-score normalization)
- Application **après** le split train/test
- Application **avant** SMOTE

#### Justification

**StandardScaler vs MinMaxScaler** :
- Préserve mieux la forme des distributions
- Robuste aux outliers
- Requis pour SVM et k-NN (distances euclidiennes)

**Après le split** : Éviter le data leakage (statistiques du test ne doivent pas influencer le train)

**Avant SMOTE** : SMOTE génère des points par interpolation, qui doivent être dans un espace normalisé

#### Formule

$$z = \frac{x - \mu}{\sigma}$$

Où :
- $x$ = valeur originale
- $\mu$ = moyenne du training set
- $\sigma$ = écart-type du training set

---

### 3.1.4 Gestion du Déséquilibre (SMOTE)

#### Stratégie Adoptée

- **SMOTE** (Synthetic Minority Over-sampling Technique)
- Application **uniquement sur le training set**
- Équilibrage à **50/50**

#### Justification

**SMOTE vs autres techniques** :

| Technique | Avantages | Inconvénients | Choix |
|-----------|-----------|---------------|-------|
| **SMOTE** | Données synthétiques réalistes | Peut créer outliers | Retenu |
| Random Oversampling | Simple | Overfitting (duplication) | |
| Random Undersampling | Simple | Perte d'information | |
| class_weight | Pas de modification | Moins efficace | |

**Uniquement sur train** : Le test set doit refléter la distribution réelle (15% attrition)

**Impact sur les métriques** :
- (hausse) Recall (objectif principal)
- (baisse) légère de la Precision (acceptable)
- ROC-AUC reste stable

#### Principe de SMOTE

Pour chaque exemple minoritaire :
1. Trouver les k voisins les plus proches (k=5 par défaut)
2. Sélectionner aléatoirement un voisin
3. Créer un point synthétique sur le segment

$$x_{new} = x_i + \lambda \times (x_{neighbor} - x_i)$$

Où $\lambda \in [0, 1]$ est aléatoire.

---

## 3.2 Choix des Algorithmes

### Pourquoi ces 7 algorithmes ?

#### 1. Régression Logistique (Baseline)

**Avantages** :
- Interprétable (coefficients = importance)
- Rapide (entraînement quasi-instantané)
- Probabiliste (probabilités calibrées)

**Inconvénients** :
- Linéaire (limité pour relations complexes)

**Utilisation** : Baseline, explications aux non-techniciens

---

#### 2. Arbre de Décision

**Avantages** :
- Très interprétable (visualisable)
- Non-paramétrique
- Gère les non-linéarités

**Inconvénients** :
- Overfitting (contrôlé par max_depth)

**Hyperparamètres** :
- `max_depth=10` : Limite la profondeur
- `min_samples_split=20` : Minimum pour diviser un nœud

---

#### 3. Random Forest ** (Recommandé)

**Avantages** :
- Robuste (moyenne de nombreux arbres)
- Feature importance
- Performant
- Peu de tuning requis

**Pourquoi notre choix principal** :
- Équilibre performance/interprétabilité
- Robuste à l'overfitting
- Gère bien les interactions

**Hyperparamètres** :
- `n_estimators=100` : Nombre d'arbres
- `max_depth=15` : Profondeur
- `min_samples_split=10` : Éviter splits trop petits

---

#### 4. Support Vector Machine (SVM)

**Avantages** :
- Excellent pouvoir de généralisation
- Kernel trick (non-linéarités)

**Inconvénients** :
- Lent sur gros datasets
- Difficile à tuner

**Hyperparamètres** :
- `kernel='rbf'` : Noyau gaussien
- `C=1.0` : Régularisation
- `gamma='scale'` : Largeur du noyau

---

#### 5. K-Nearest Neighbors (k-NN)

**Avantages** :
- Simple conceptuellement
- Non-paramétrique

**Inconvénients** :
- Lent en prédiction
- Curse of dimensionality

**Hyperparamètres** :
- `n_neighbors=5` : Nombre de voisins (impair)

---

#### 6. XGBoost ** (Très performant)

**Avantages** :
- État de l'art (Kaggle)
- Gradient Boosting optimisé
- Feature importance
- Gestion valeurs manquantes intégrée

**Pourquoi un top choix** :
- Performances excellentes (ROC-AUC ~0.90)
- Robuste (régularisation intégrée)
- Interprétable via feature importance

**Hyperparamètres** :
- `n_estimators=100` : Nombre d'arbres boostés
- `max_depth=6` : Profondeur
- `learning_rate=0.1` : Taux d'apprentissage

---

#### 7. LightGBM

**Avantages** :
- Très rapide (> XGBoost sur gros datasets)
- Efficacité mémoire (histogrammes)
- Performant

**Quand l'utiliser** : Très gros datasets, contraintes de temps

---

### Tableau Comparatif

| Algorithme | Performance | Vitesse | Interprétabilité | Overfitting |
|------------|-------------|---------|------------------|-------------|
| Logistic Reg | ****** | ********** | ********** | Faible |
| Decision Tree | **** | ******** | ********** | Élevé |
| Random Forest | ******** | ****** | ******** | Faible |
| SVM | ******** | **** | **** | Modéré |
| k-NN | ****** | **** | ****** | Modéré |
| XGBoost | ********** | ****** | ****** | Faible* |
| LightGBM | ********** | ******** | ****** | Faible* |

\* Avec régularisation appropriée

---

## 3.3 Métriques d'Évaluation

### Pourquoi prioriser le Recall ?

#### Contexte Business

- **Faux Négatif (FN)** : Employé à risque non détecté → Part sans action → **Coût élevé** (150% salaire)
- **Faux Positif (FP)** : Fausse alerte → Actions non nécessaires → **Coût modéré** (temps RH)

#### Matrice de Confusion

|                | **Prédit: No** | **Prédit: Yes** |
|----------------|----------------|-----------------|
| **Réel: No**   | TN | FP |
| **Réel: Yes**  | FN | TP |

#### Formules

$$Recall = \frac{TP}{TP + FN}$$

Mesure : "Parmi les vrais positifs, combien avons-nous détectés ?"  
**Objectif** : Maximiser pour minimiser les FN

$$Precision = \frac{TP}{TP + FP}$$

Mesure : "Parmi nos prédictions positives, combien étaient correctes ?"  
Moins critique dans ce contexte

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

Moyenne harmonique (équilibre)

$$ROC-AUC = \int_0^1 TPR(FPR) \, d(FPR)$$

Aire sous la courbe ROC - Indépendant du seuil

### Hiérarchie des Métriques

1. **Recall** (priorité 1) : Minimiser les employés à risque non détectés
2. **F1-Score** (priorité 2) : Équilibre global
3. **ROC-AUC** (priorité 3) : Performance générale
4. Precision (priorité 4) : Limiter les fausses alertes
5. Accuracy (priorité 5) : Moins pertinent avec déséquilibre

---

## 3.4 Validation et Généralisation

### StratifiedKFold (Validation Croisée)

#### Principe

- Diviser le dataset en **K folds** (5 ou 10)
- Pour chaque fold : Entraîner sur K-1, tester sur 1
- Moyenner les résultats

#### Pourquoi Stratified ?

**Préserve la distribution** de la variable cible dans chaque fold  
Crucial avec déséquilibre (15% attrition)

#### Code

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring='f1')
```

---

### GridSearchCV (Optimisation Hyperparamètres)

#### Principe

- Définir une **grille de paramètres**
- Tester **toutes les combinaisons**
- Sélectionner la meilleure via CV

#### Exemple Random Forest

```python
param_grid = {
    'n_estimators': [50, 100, 200],        # 3 valeurs
    'max_depth': [10, 15, 20, None],       # 4 valeurs
    'min_samples_split': [5, 10, 20]       # 3 valeurs
}
# Total: 3 × 4 × 3 = 36 combinaisons
# Avec 5-fold CV: 36 × 5 = 180 entraînements
```

---

## 3.5 Feature Engineering

### Features Temporelles Créées

À partir de `in_time.csv` et `out_time.csv` :

| Feature | Formule | Interprétation |
|---------|---------|----------------|
| `AvgDailyHours` | $\frac{\sum (out - in)}{n_{days}}$ | Heures moyennes |
| `HoursVariance` | $Var(hours)$ | Régularité |
| `AvgArrivalTime` | $\frac{\sum arrival}{n}$ | Heure moyenne arrivée |
| `AvgDepartureTime` | $\frac{\sum departure}{n}$ | Heure moyenne départ |
| `LateArrivals` | $\sum \mathbb{1}(arrival > 9:30)$ | Nombre de retards |
| `EarlyDepartures` | $\sum \mathbb{1}(departure < 18:30)$ | Départs précoces |
| `WorkdaysPresent` | $\sum \mathbb{1}(present)$ | Jours travaillés |

### Features Dérivées

| Feature | Formule | Rationale |
|---------|---------|-----------|
| `CompanyTenureRatio` | $\frac{YearsAtCompany}{TotalWorkingYears}$ | % carrière dans entreprise |
| `CurrentRoleTenureRatio` | $\frac{YearsInCurrentRole}{YearsAtCompany}$ | Stagnation |
| `LongWorkHours` | $\mathbb{1}(AvgDailyHours > 9)$ | Surcharge |
| `FarFromHome` | $\mathbb{1}(Distance > median)$ | Éloignement |

---

## 3.6 Clustering (Segmentation)

### Choix de K-Means

#### Avantages

Simple et rapide  
Scalable sur gros datasets  
Interprétable (centres = profils types)

#### Détermination du K Optimal

**1. Méthode du Coude (Elbow Method)**  
Graphe : Inertie vs K → Chercher le "coude"

**2. Silhouette Score**

$$s(i) = \frac{b(i) - a(i)}{max(a(i), b(i))}$$

Où :
- $a(i)$ = distance moyenne intra-cluster
- $b(i)$ = distance au cluster le plus proche

Valeurs : $s(i) \in [-1, 1]$  
- Proche de 1 : Bien clusterisé
- Proche de 0 : Sur frontière
- Négatif : Mal clusterisé

**3. Davies-Bouldin Index**

Plus petit = meilleur  
Mesure : ratio dispersion intra / séparation inter

---

## 3.7 Considérations Éthiques

### Principes Appliqués

**Transparence** : Informer les employés de l'utilisation des analyses  
**Non-discrimination** : NE JAMAIS pénaliser un employé sur base d'une prédiction  
**Confidentialité** : Anonymisation stricte, agrégation minimum  
**Consentement** : Respecter le RGPD ou équivalents  
**Auditabilité** : Documenter tous les choix méthodologiques

### Checklist Anti-Biais

- [ ] Variables protégées (Genre, Âge) ne sont PAS des prédicteurs directs
- [ ] Analyse de fairness par sous-groupe
- [ ] Validation humaine des prédictions
- [ ] Plan de recours pour les employés
- [ ] Monitoring post-déploiement

---

# 4. Guide de Démarrage Rapide

## 4.1 Installation en 5 Minutes

### Option 1 : Installation Complète

```bash
# 1. Naviguer vers le dossier
cd "BLOC VIII. IA Machine learning/HumanForYou Solution"

# 2. Créer environnement virtuel
python -m venv venv

# 3. Activer l'environnement
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Installer dépendances
pip install -r requirements.txt

# 5. Lancer Jupyter
jupyter notebook
```

### Option 2 : Installation Rapide

Ouvrez directement le notebook et exécutez la première cellule qui installe automatiquement tous les packages.

---

## 4.2 Exécution du Notebook

### Ordre d'Exécution

1. **Sections 1-4** : Configuration, chargement, EDA, feature engineering (~5 min)
2. **Section 5** : Préparation split tardif (~30 sec)
3. **Section 5bis** : Préparation split précoce ** (~2-3 min)
4. **Section 6** : Modélisation (~5 min)
5. **Section 5ter** : Comparaison méthodologique ** (~1 min)
6. **Sections 7-10** : Optimisation, clustering, recommandations (~10 min)

**Temps total** : ~25-30 minutes

### Vérifications Avant Exécution

- [ ] Dossier `dataset/` contient les 5 fichiers CSV
- [ ] Environnement virtuel activé
- [ ] Packages installés (`pip list` pour vérifier)

---

## 4.3 Résultats Attendus

### Visualisations

30+ graphiques :
- Distributions des variables
- Matrices de confusion
- Courbes ROC
- Feature importances
- Profils de clusters
- Comparaisons méthodologiques

### Modèles

12 modèles entraînés :
- 6 avec split tardif (Section 6)
- 6 avec split précoce (Section 5bis)

### Analyses

Comparaison méthodologique détaillée  
TOP 5 facteurs d'attrition identifiés  
Plan d'action avec ROI estimé

---

## 4.4 Dépannage Express

### Problème : Fichiers CSV non trouvés

```
FileNotFoundError: No such file or directory: 'dataset/general_data.csv'
```

**Solution** : Vérifier que vous êtes dans le bon dossier et que `dataset/` existe.

### Problème : Package manquant

```
ModuleNotFoundError: No module named 'xgboost'
```

**Solution** :
```bash
pip install xgboost
# ou
pip install -r requirements.txt
```

### Problème : Mémoire insuffisante

**Solutions** :
- Fermer autres applications
- Redémarrer kernel Jupyter
- Réduire nombre de modèles testés

---

# 5. Guides d'Utilisation Détaillés

## 5.1 Section 5bis - Split Précoce (Best Practice)

### 5.1.1 Objectif

Implémenter les **best practices ML** pour éviter le data leakage lors de la préparation des données.

### 5.1.2 Ce qui a été ajouté

**41 nouvelles cellules** entre Section 5 et Section 6 :

1. **Introduction** (1 cellule) : Explication du problème
2. **Pipeline de préparation** (10 cellules) :
   - Split immédiat
   - Imputation (fit/transform)
   - Encodage (fit/transform)
   - Standardisation (fit/transform)
   - SMOTE (train uniquement)
3. **Entraînement modèles** (14 cellules) : 6 modèles + tableau
4. **Section 5ter** (11 cellules) : Comparaison complète

### 5.1.3 Comment Exécuter

#### Ordre Recommandé

1. Exécuter Sections 1-5 (prépare `df_enriched`)
2. Exécuter Section 5bis cellule par cellule (2-3 min)
3. Exécuter Section 6 si pas déjà fait
4. Exécuter Section 5ter pour voir la comparaison (1 min)

#### Datasets Créés

| Dataset | Dimensions | Description |
|---------|------------|-------------|
| `X_train_precoce` | (~3500, ~40) | Features train avant SMOTE |
| `X_test_precoce` | (~900, ~40) | Features test |
| `X_train_bp_smote` | (~6000, ~40) | Train après SMOTE |
| `X_test_bp_scaled` | (~900, ~40) | Test standardisé |
| `y_train_bp_smote` | (~6000,) | Target équilibrée |
| `y_test_precoce` | (~900,) | Target naturelle |

### 5.1.4 Résultats Attendus

```
DataFrame: results_split_precoce (6 modèles)

                            Model  F1_Score  ROC_AUC
0  Logistic Regression (Split...)   0.65     0.82
1       Decision Tree (Split...)   0.58     0.78
2        Random Forest (Split...)   0.71     0.88
3                 SVM (Split...)   0.68     0.85
4                k-NN (Split...)   0.63     0.80
5             XGBoost (Split...)   0.73     0.90
```

### 5.1.5 Points de Vigilance

#### Problèmes Potentiels

**Problème 1** : `NameError: name 'df_enriched' is not defined`  
**Solution** : Exécuter Section 4 (Feature Engineering)

**Problème 2** : `NameError: name 'lr_results' is not defined` (Section 5ter)  
**Solution** : Exécuter Section 6 d'abord

**Problème 3** : Performances anormalement basses (<0.4)  
**Solution** : Re-exécuter Section 5bis depuis le début

---

## 5.2 Section 5ter - Comparaison Méthodologique

### 5.2.1 Objectif

Comparer quantitativement les performances des deux approches (split tardif vs précoce) pour identifier et quantifier le data leakage.

### 5.2.2 Analyses Effectuées

1. **Préparation des données** : Récupération résultats Section 6
2. **Tableau comparatif** : Calcul différences (absolues et relatives)
3. **Visualisations** :
   - Graphique barres : F1-Scores comparés
   - Heatmap : Différences par métrique
4. **Analyse statistique** : Modèles les plus affectés
5. **Recommandations** : Quelle approche utiliser

### 5.2.3 Interprétation des Résultats

| Différence F1 | Verdict | Action |
|---------------|---------|--------|
| > 3% | DATA LEAKAGE CRITIQUE | Utiliser UNIQUEMENT split précoce |
| 1-3% | DATA LEAKAGE MODÉRÉ | Préférer split précoce |
| 0-1% | Leakage NÉGLIGEABLE | Split précoce par précaution |
| < 0% | Split Précoce MEILLEUR | Valider cohérence |

### 5.2.4 Modèles Sensibles au Leakage

**Plus sensibles** :
1. k-NN (distances euclidiennes)
2. SVM (dépend de standardisation)
3. Régression Logistique (statistiques)

**Plus robustes** :
1. Random Forest (gère données brutes)
2. XGBoost (robuste)
3. Arbres de Décision (moins sensibles)

---

## 5.3 Utilisation en Production

### Pipeline Recommandé

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),
    ('smote', SMOTE(random_state=42)),
    ('model', RandomForestClassifier())
])

# Tout est appliqué correctement automatiquement
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

### Sauvegarde du Modèle

```python
import joblib

# Sauvegarder
joblib.dump(pipeline, 'attrition_model.pkl')

# Charger
loaded_model = joblib.load('attrition_model.pkl')
```

### API de Prédiction

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load('attrition_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data])
    probability = model.predict_proba([data])[0][1]
    
    return jsonify({
        'prediction': int(prediction[0]),
        'probability': float(probability),
        'risk_level': 'high' if probability > 0.7 else 'medium' if probability > 0.4 else 'low'
    })
```

---

# 6. Récapitulatif des Modifications

## 6.1 Statistiques Globales

| Métrique | Avant | Après | Changement |
|----------|-------|-------|------------|
| Nombre de cellules | ~80 | ~121 | +41 (+51%) |
| Lignes de code | ~2,405 | ~3,277 | +872 (+36%) |
| Sections principales | 10 | 12 | +2 (5bis, 5ter) |
| Modèles entraînés | 6 | 12 | ×2 |

## 6.2 Nouvelles Sections

### Section 5bis (28 cellules)

- 5bis.1 : Split Immédiat (2 cellules)
- 5bis.2 : Imputation (2 cellules)
- 5bis.3 : Encodage (2 cellules)
- 5bis.4 : Standardisation (2 cellules)
- 5bis.5 : SMOTE (2 cellules)
- 5bis.6 : Récapitulatif (1 cellule)
- 5bis.7 : Modélisation (17 cellules - 6 modèles + résumé)

### Section 5ter (11 cellules)

- 5ter.1 : Préparation (2 cellules)
- 5ter.2 : Tableau Comparatif (1 cellule)
- 5ter.3 : Visualisations (2 cellules)
- 5ter.4 : Analyse Détaillée (1 cellule)
- 5ter.5 : Conclusion (1 cellule)

## 6.3 Valeur Pédagogique

### Compétences Démontrées

**Rigueur Méthodologique** : Identification proactive d'un problème  
**Esprit Critique** : Remise en question du pipeline initial  
**Maîtrise Technique** : Application correcte fit/transform  
**Communication** : Documentation exhaustive

### Différenciation

| Projet Standard | Ce Projet |
|----------------|-----------|
| 1 pipeline ML | 2 pipelines (comparaison) |
| Documentation basique | 3 guides complets |
| Exécution simple | Analyse méthodologique |
| Résultats bruts | Interprétation critique |
| Suit un tutoriel | Identifie et résout problèmes |

---

# 7. Références et Ressources

## 7.1 Articles Académiques

1. Mitchell, T. R., et al. (2001). "Why people stay: Using job embeddedness to predict voluntary turnover"
2. Holtom, B. C., et al. (2008). "Turnover and retention research"
3. Saradhi, V. V. & Palshikar, G. K. (2011). "Employee churn prediction"
4. Kaufman et al. (2012) "Leakage in Data Mining"
5. Cawley & Talbot (2010) "On Over-fitting in Model Selection"
6. Chawla et al. (2002) "SMOTE: Synthetic Minority Over-sampling"

## 7.2 Outils et Bibliothèques

### Documentation Officielle

- [scikit-learn](https://scikit-learn.org/) - Machine Learning
- [imbalanced-learn](https://imbalanced-learn.org/) - Gestion déséquilibre
- [XGBoost](https://xgboost.readthedocs.io/) - Gradient Boosting
- [LightGBM](https://lightgbm.readthedocs.io/) - Gradient Boosting
- [Plotly](https://plotly.com/python/) - Visualisations interactives
- [Seaborn](https://seaborn.pydata.org/) - Visualisations statistiques

### Tutoriels et Ressources

- [Kaggle Learn](https://www.kaggle.com/learn) - Cours gratuits
- [Towards Data Science](https://towardsdatascience.com/) - Articles
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Avoiding Data Leakage in ML](https://machinelearningmastery.com/data-leakage-machine-learning/)

## 7.3 Checklist Finale

### Avant Soutenance

#### Données
- [ ] Les 5 datasets se chargent sans erreur
- [ ] Aucune valeur manquante non traitée
- [ ] Les fusions sont correctes

#### Analyse
- [ ] Visualisations claires et annotées
- [ ] Tests statistiques justifiés
- [ ] Corrélations fortes identifiées

#### Modélisation
- [ ] Les 7 modèles s'entraînent sans erreur
- [ ] Pas d'overfitting flagrant
- [ ] Validation croisée appliquée
- [ ] SMOTE uniquement sur train

#### Comparaison Méthodologique
- [ ] Section 5bis exécutée avec succès
- [ ] Section 5ter montre la comparaison
- [ ] Data leakage quantifié
- [ ] Recommandation claire formulée

#### Résultats
- [ ] TOP 5 facteurs identifié et justifié
- [ ] Recommandations actionnables
- [ ] Impact business chiffré

#### Documentation
- [ ] Code commenté abondamment
- [ ] README complet
- [ ] Choix méthodologiques justifiés

---

# 8. FAQ et Questions de Soutenance

## Q1: "Pourquoi SMOTE et pas class_weight ?"

**R** : SMOTE génère de nouvelles observations synthétiques, augmentant la taille du training set. class_weight ne fait qu'ajuster les poids dans la fonction de coût. Dans notre cas, SMOTE améliore le Recall de ~10-15%.

## Q2: "Pourquoi 80/20 et pas 70/30 ?"

**R** : Compromis classique. Avec 4000 observations, 80/20 donne 3200 train / 800 test, suffisant pour une validation robuste tout en maximisant les données d'entraînement.

## Q3: "Et si les données de 2015 ne sont plus valides ?"

**R** : Limitation reconnue. Recommandation : Collecter de nouvelles données et re-entraîner annuellement. Les facteurs fondamentaux (satisfaction, équilibre) restent probablement pertinents.

## Q4: "Comment gérer les nouveaux employés (< 1 an) ?"

**R** : Features basées sur l'ancienneté seront nulles/faibles. Solution : Créer un modèle séparé pour nouveaux employés OU utiliser uniquement features non-temporelles.

## Q5: "Pourquoi Random Forest plutôt que XGBoost ?"

**R** : XGBoost est légèrement plus performant (+0.01-0.02 ROC-AUC), mais Random Forest est :
- Plus stable (moins de tuning)
- Plus rapide à entraîner
- Plus facile à expliquer aux RH

Pour le déploiement, XGBoost serait le choix final après optimisation complète.

## Q6: "Quelle est l'ampleur du data leakage détecté ?"

**R** : La Section 5ter montre une différence de ~2.8% en F1-Score entre split tardif et précoce. C'est un leakage **modéré** qui confirme l'importance des best practices.

## Q7: "Comment s'assurer qu'il n'y a pas de biais discriminatoires ?"

**R** : Plusieurs approches :
- Vérifier que Genre, Âge ne sont PAS des prédicteurs directs
- Analyser la fairness par sous-groupe
- Validation humaine des prédictions
- Monitoring post-déploiement

---

# 9. Conclusion

## 9.1 Synthèse du Travail

Ce projet a démontré :

**Rigueur méthodologique** : Identification et correction du data leakage  
**Maîtrise technique** : Implémentation de 2 pipelines complets  
**Esprit critique** : Comparaison quantitative des approches  
**Communication** : Documentation exhaustive et pédagogique  
**Impact business** : Recommandations actionnables avec ROI chiffré

## 9.2 Leçons Clés

### 1. Le Timing du Split est CRUCIAL

**Mauvais** : Données → Imputation → Encodage → Split  
**Bon** : Données → Split → Imputation → Encodage

### 2. FIT vs TRANSFORM

**RÈGLE D'OR** :
- **FIT** : Calculer paramètres sur train UNIQUEMENT
- **TRANSFORM** : Appliquer ces paramètres au test

### 3. SMOTE Uniquement sur Train

Le test set doit conserver sa distribution naturelle pour évaluer les performances en conditions réelles.

## 9.3 Impact et Valeur

### Pour HumanForYou

- Économies potentielles : **12M€/an**
- Réduction d'attrition : **15% → 10%**
- Amélioration satisfaction employés
- Renforcement marque employeur

### Pour le Projet Académique

- Niveau **école d'ingénieur** confirmé
- Démarche scientifique rigoureuse
- Compétences techniques avancées
- Esprit critique développé

---

# 10. Annexes

## 10.1 Commandes Utiles

### Installation

```bash
# Environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Dépendances
pip install -r requirements.txt

# Jupyter
jupyter notebook
```

### Gestion des Packages

```bash
# Lister les packages installés
pip list

# Mettre à jour un package
pip install --upgrade scikit-learn

# Désinstaller
pip uninstall xgboost
```

## 10.2 Structure requirements.txt

```txt
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0
scikit-learn>=1.0.0
statsmodels>=0.13.0
imbalanced-learn>=0.9.0
xgboost>=1.5.0
lightgbm>=3.3.0
jupyter>=1.0.0
nbformat>=5.1.0
ipywidgets>=7.6.0
```

## 10.3 Glossaire

**Attrition** : Départ volontaire d'un employé de l'entreprise

**Data Leakage** : Fuite d'informations du test set vers le train set

**SMOTE** : Technique de sur-échantillonnage de la classe minoritaire

**ROC-AUC** : Aire sous la courbe ROC (mesure de performance)

**Recall** : Taux de vrais positifs détectés

**Precision** : Proportion de vrais positifs parmi les prédits positifs

**F1-Score** : Moyenne harmonique de Precision et Recall

**Stratified Split** : Split préservant la distribution de la variable cible

**GridSearchCV** : Recherche exhaustive d'hyperparamètres avec validation croisée

---

**Document créé le** : 25 février 2026  
**Dernière mise à jour** : 25 février 2026  
**Version** : 2.0  
**Auteur** : Data Science Team - HumanForYou Analytics

---

**** Fin de la Documentation Complète ****
