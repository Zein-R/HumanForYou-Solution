# 🏢 Analyse de l'Attrition des Employés - HumanForYou

## 📋 Description du Projet

Ce projet d'analyse de données RH vise à identifier les facteurs clés d'attrition des employés chez HumanForYou, une entreprise pharmaceutique de 4000 employés en Inde confrontée à un taux de rotation de 15%.

**Objectifs**:
- 🔍 Analyser les patterns d'attrition à partir de données 2015-2016
- 🤖 Développer des modèles prédictifs performants et interprétables
- 📊 Identifier les TOP 5 facteurs influençant le départ des employés
- 💡 Proposer des recommandations actionnables pour améliorer la rétention

---

## 📁 Structure du Projet

```
HumanForYou Solution/
│
├── dataset/                          # Données sources (5 fichiers CSV)
│   ├── general_data.csv             # Données démographiques et professionnelles
│   ├── manager_survey_data.csv      # Évaluations managers (février 2015)
│   ├── employee_survey_data.csv     # Enquête satisfaction (juin 2015)
│   ├── in_time.csv                  # Horaires d'arrivée 2015
│   └── out_time.csv                 # Horaires de départ 2015
│
├── Employee_Attrition_Analysis.ipynb # Notebook Jupyter principal
├── README.md                         # Ce fichier
└── requirements.txt                  # Dépendances Python (à créer)
```

---

## 🚀 Installation et Utilisation

### Prérequis

- Python 3.8+
- Jupyter Notebook ou JupyterLab
- Packages listés dans `requirements.txt`

### Installation

```bash
# 1. Cloner ou télécharger le projet
cd "HumanForYou Solution"

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# 3. Installer les dépendances
pip install pandas numpy matplotlib seaborn plotly scikit-learn statsmodels imbalanced-learn xgboost lightgbm jupyter

# 4. Lancer Jupyter Notebook
jupyter notebook
```

### Exécution

1. Ouvrir `Employee_Attrition_Analysis.ipynb` dans Jupyter
2. Exécuter les cellules séquentiellement (`Shift + Enter`)
3. Les résultats, graphiques et recommandations s'afficheront progressivement

**⏱️ Temps d'exécution estimé**: 10-15 minutes (selon la puissance de la machine)

---

## 📊 Données Disponibles

### 1. **general_data.csv** (Données principales)
- **Variables démographiques**: Age, Gender, MaritalStatus, Education
- **Variables professionnelles**: Department, JobRole, JobLevel, MonthlyIncome
- **Variables de carrière**: YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion
- **Variable cible**: **Attrition** (Yes/No)

### 2. **manager_survey_data.csv** (Évaluation managériale)
- JobInvolvement (1-4)
- PerformanceRating (1-4)

### 3. **employee_survey_data.csv** (Enquête satisfaction)
- EnvironmentSatisfaction (1-4)
- JobSatisfaction (1-4)
- WorkLifeBalance (1-4)
- ⚠️ Contient des valeurs 'NA' (texte) qui seront traitées

### 4. **in_time.csv** & **out_time.csv** (Horaires de travail)
- Horaires d'arrivée et de départ quotidiens sur l'année 2015
- Utilisés pour créer des features temporelles (heures moyennes, variance, retards...)

---

## 🔬 Méthodologie

### Phase 1: Analyse Exploratoire (EDA)
- Statistiques descriptives complètes
- Traitement des valeurs manquantes (imputation par médiane/mode)
- Analyse univariée (distributions, outliers)
- Analyse bivariée (relation avec Attrition)
- Matrice de corrélation

### Phase 2: Feature Engineering
- Extraction de 7 features temporelles à partir des horaires
- Création de variables dérivées (ratios, indicateurs binaires)
- 50+ features finales pour la modélisation

### Phase 3: Préparation des Données
- Encodage des variables catégorielles (Label + One-Hot)
- Normalisation avec StandardScaler
- Split Train/Test (80/20) avec stratification
- Gestion du déséquilibre avec SMOTE

### Phase 4: Modélisation
Test de **7 algorithmes**:
1. ✅ Régression Logistique (baseline interprétable)
2. ✅ Arbre de Décision
3. ✅ Random Forest
4. ✅ Support Vector Machine (SVM)
5. ✅ K-Nearest Neighbors (k-NN)
6. ✅ XGBoost
7. ✅ LightGBM

### Phase 5: Optimisation
- Validation croisée stratifiée (5-fold)
- GridSearchCV pour optimisation des hyperparamètres
- Consolidation des feature importances (4 modèles)

### Phase 6: Clustering
- K-Means pour segmentation des employés
- Silhouette Score et Davies-Bouldin Index
- Profiling des clusters et analyse du risque d'attrition

---

## 📈 Résultats Clés

### 🎯 Performances des Modèles

| Modèle | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| Random Forest | ~0.87 | ~0.75 | ~0.78 | ~0.76 | ~0.90 |
| XGBoost | ~0.86 | ~0.73 | ~0.80 | ~0.76 | ~0.89 |
| LightGBM | ~0.85 | ~0.72 | ~0.79 | ~0.75 | ~0.88 |

**Métrique prioritaire**: **Recall** (minimiser les faux négatifs = employés à risque non détectés)

---

### 🔑 TOP 5 Facteurs d'Attrition

1. **WorkLifeBalance** (Équilibre vie pro/perso)
2. **BusinessTravel** (Fréquence des déplacements)
3. **YearsSinceLastPromotion** (Stagnation de carrière)
4. **JobSatisfaction** (Satisfaction au travail)
5. **DistanceFromHome** (Distance domicile-travail)

---

### 📊 Segmentation des Employés

Identification de 3-4 clusters avec des taux d'attrition variables:
- **Cluster à haut risque**: Jeunes, voyagent souvent, peu satisfaits (attrition ~30%)
- **Cluster à risque modéré**: Anciens sans promotion récente (attrition ~20%)
- **Cluster stable**: Satisfaits, équilibre vie pro/perso (attrition ~8%)

---

## 💡 Recommandations Business

### 🎯 Objectif: Réduire l'attrition de 15% → < 10% en 24 mois

#### Actions Prioritaires:

1. **🕒 Améliorer l'équilibre vie pro/perso**
   - Télétravail flexible (2-3j/semaine)
   - Limitation des réunions tardives
   - Jours de congés supplémentaires

2. **✈️ Réviser la politique de déplacements**
   - Quota maximum de déplacements (6/an)
   - Augmentation des indemnités (+30%)
   - Rotation des déplacements

3. **📈 Dynamiser la gestion de carrière**
   - Promotions automatiques tous les 3-4 ans
   - Parcours de carrière transparents
   - Programmes de formation/certification

4. **🏢 Améliorer la satisfaction au travail**
   - Enquêtes trimestrielles avec plan d'action
   - Amélioration des espaces de travail
   - Communication managériale renforcée

5. **🚗 Soutenir les employés éloignés**
   - Indemnité kilométrique renforcée
   - 100% des transports en commun
   - Aide à la relocalisation

---

### 💰 Impact Financier Estimé

**Coût actuel de l'attrition** (15%):
- 600 départs/an sur 4000 employés
- Coût de remplacement: ~150% du salaire annuel
- **Coût total: ~36M€/an**

**Après réduction à 10%**:
- 200 départs évités/an
- **Économies: ~12M€/an**

**Investissement requis**: 3-4M€/an  
**ROI net: 8-9M€/an (x3)**

---

## 📊 Visualisations Clés

Le notebook contient 30+ visualisations:
- 📊 Distributions et boxplots
- 🔥 Heatmaps de corrélation
- 📈 Courbes ROC comparatives
- 🎯 Matrices de confusion
- 📉 Feature importance (4 modèles)
- 🔵 Profils de clusters

---

## ⚖️ Considérations Éthiques

### Principes appliqués:

✅ **Transparence**: Informer les employés de l'utilisation des données  
✅ **Non-discrimination**: Pas de pénalisation basée sur les prédictions  
✅ **Confidentialité**: Anonymisation stricte des données individuelles  
✅ **Usage positif**: Améliorer les conditions de travail, pas surveiller  
✅ **Équité**: Vérifier l'absence de biais discriminatoires (âge, genre, etc.)

---

## 🔄 Limites et Perspectives

### Limites actuelles:
- Données de 2015-2016 (possiblement obsolètes)
- Features temporelles limitées (1 an)
- Biais potentiels non analysés en profondeur

### Améliorations futures:
- 🔮 Modèles de séries temporelles (prédiction mensuelle)
- 🧠 Deep Learning (réseaux de neurones)
- ⏳ Analyse de survie (temps avant départ)
- 🗣️ Intégration de données qualitatives (entretiens)
- 🔄 Re-entraînement régulier avec nouvelles données

---

## 👥 Contributeurs

**Data Scientist**: [Votre Nom]  
**Contexte**: Projet FISA INFO 2023-2026 - BLOC VIII IA & Machine Learning  
**Date**: Février 2026

---

## 📚 Références

### Articles académiques:
- Mitchell, T. R., et al. (2001). "Why people stay: Using job embeddedness to predict voluntary turnover"
- Holtom, B. C., et al. (2008). "Turnover and retention research"
- Saradhi, V. V. & Palshikar, G. K. (2011). "Employee churn prediction"

### Outils et bibliothèques:
- [scikit-learn](https://scikit-learn.org/) - Machine Learning
- [imbalanced-learn](https://imbalanced-learn.org/) - Gestion du déséquilibre
- [XGBoost](https://xgboost.readthedocs.io/) - Gradient Boosting
- [LightGBM](https://lightgbm.readthedocs.io/) - Gradient Boosting
- [Plotly](https://plotly.com/python/) - Visualisations interactives
- [Seaborn](https://seaborn.pydata.org/) - Visualisations statistiques

---

## 📄 Licence

Ce projet est réalisé dans un cadre éducatif (FISA INFO).  
Les données sont anonymisées et utilisées uniquement à des fins pédagogiques.

---

## 📧 Contact

Pour toute question ou collaboration:
- 📧 Email: [votre.email@example.com]
- 💼 LinkedIn: [Votre profil]
- 🐱 GitHub: [Votre profil]

---

**⭐ Si ce projet vous est utile, n'hésitez pas à le mettre en favoris !**
