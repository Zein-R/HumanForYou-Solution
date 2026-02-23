# 📘 Guide d'Utilisation de la Section 5bis - Split Précoce (Best Practice)

## 🎯 Objectif

La **Section 5bis** implémente les **best practices de Machine Learning** pour éviter le **data leakage** lors de la préparation des données. Elle complète la Section 5 originale et permet une comparaison méthodologique approfondie.

---

## 📊 Ce qui a été ajouté au notebook

### ✅ Section 5bis: Préparation des Données avec Split Précoce (Best Practice)

**41 nouvelles cellules** ajoutées entre la Section 5 et la Section 6, comprenant :

#### 1. Introduction et Explication (1 cellule Markdown)
- Problème méthodologique identifié
- Explication du data leakage
- Solution proposée (split précoce)

#### 2. Pipeline de Préparation (10 cellules)
- **Cellule 5bis.1** : Split immédiat (AVANT toute transformation)
- **Cellule 5bis.2** : Imputation (FIT sur train, TRANSFORM sur test)
- **Cellule 5bis.3** : Encodage (FIT sur train, TRANSFORM sur test)
- **Cellule 5bis.4** : Standardisation (FIT sur train, TRANSFORM sur test)
- **Cellule 5bis.5** : SMOTE (train uniquement)
- **Cellule 5bis.6** : Récapitulatif du pipeline

#### 3. Entraînement des Modèles (14 cellules)
- Régression Logistique
- Arbre de Décision
- Random Forest
- SVM (Support Vector Machine)
- k-NN (k-Nearest Neighbors)
- XGBoost
- Tableau récapitulatif des résultats

#### 4. Section 5ter: Comparaison Split Tardif vs Split Précoce (11 cellules)
- Préparation des données de comparaison
- Tableau comparatif détaillé
- 2 visualisations :
  * Comparaison des F1-Scores (barres)
  * Heatmap des différences
- Analyse statistique approfondie
- Interprétation et recommandations

---

## 🚀 Comment Exécuter la Section 5bis

### Option 1: Exécution Séquentielle (Recommandé)

1. **Exécuter toutes les cellules jusqu'à la Section 5** (incluse)
   - Cela prépare `df_enriched` qui est nécessaire

2. **Exécuter la Section 5bis** cellule par cellule
   - Suivez l'ordre des cellules
   - Chaque cellule affiche des informations sur son traitement
   - **Temps estimé** : 2-3 minutes pour toute la section

3. **Exécuter la Section 5ter (Comparaison)**
   - ⚠️ **IMPORTANT** : Cette section nécessite que la Section 6 (modélisation originale) ait été exécutée pour créer les variables `lr_results`, `dt_results`, `rf_results`, etc.
   - Si ce n'est pas le cas, la section affichera un avertissement mais ne plantera pas

### Option 2: Exécution Ciblée

Si vous avez déjà exécuté le notebook jusqu'à la Section 6, vous pouvez :

1. **Re-exécuter la Section 5bis directement** (si `df_enriched` existe)
2. **Exécuter immédiatement la Section 5ter** pour voir la comparaison

---

## 📈 Résultats Attendus

### A. Datasets Créés (Section 5bis)

| Dataset | Dimensions | Description | Utilisation |
|---------|------------|-------------|-------------|
| `X_train_precoce` | (~3500, ~40) | Features train (avant SMOTE) | Inspection |
| `X_test_precoce` | (~900, ~40) | Features test (avant transformations) | Inspection |
| `X_train_bp_smote` | (~6000, ~40) | Features train après SMOTE | Entraînement |
| `X_test_bp_scaled` | (~900, ~40) | Features test standardisées | Évaluation |
| `y_train_bp_smote` | (~6000,) | Target train équilibrée | Entraînement |
| `y_test_precoce` | (~900,) | Target test naturelle | Évaluation |

### B. Résultats des Modèles (Section 5bis)

Un DataFrame `results_split_precoce` contenant :
- Model (nom du modèle)
- Train_Accuracy
- Test_Accuracy
- Precision
- Recall
- F1_Score ⭐ (métrique principale)
- ROC_AUC

**Exemple de résultats attendus** :

```
                               Model  F1_Score  ROC_AUC
0  Logistic Regression (Split Précoce)   0.65     0.82
1       Decision Tree (Split Précoce)   0.58     0.78
2        Random Forest (Split Précoce)   0.71     0.88
3                 SVM (Split Précoce)   0.68     0.85
4                k-NN (Split Précoce)   0.63     0.80
5             XGBoost (Split Précoce)   0.73     0.90
```

### C. Comparaison (Section 5ter)

Un DataFrame `comparison_df` montrant :
- Performances Split Tardif (Section 5)
- Performances Split Précoce (Section 5bis)
- Différences (en points de pourcentage)
- Différences relatives (en %)

**Interprétation** :
- **Différence positive** (>2%) → Data leakage détecté (Split Tardif surestimé)
- **Différence proche de 0** (±1%) → Pas de leakage significatif
- **Différence négative** → Split Précoce meilleur (rare, mais possible)

---

## 🔍 Points Clés à Vérifier

### ✅ Checklist d'Exécution Réussie

- [ ] `df_enriched` existe avant d'exécuter la Section 5bis
- [ ] `X_train_bp_smote` a une forme ~(6000, 40) après SMOTE
- [ ] `y_train_bp_smote` est équilibré (50/50)
- [ ] `X_test_bp_scaled` garde sa distribution naturelle
- [ ] `results_split_precoce` contient 6 lignes (6 modèles)
- [ ] Les F1-Scores sont entre 0.5 et 0.9 (valeurs réalistes)
- [ ] La comparaison affiche des différences < 5% en général

### ⚠️ Problèmes Potentiels et Solutions

#### Problème 1: `NameError: name 'df_enriched' is not defined`
**Cause** : Section 4 (Feature Engineering) n'a pas été exécutée  
**Solution** : Exécuter toutes les cellules de la Section 4 qui créent `df_enriched`

#### Problème 2: `NameError: name 'lr_results' is not defined` (Section 5ter)
**Cause** : Section 6 (modélisation originale) n'a pas encore été exécutée  
**Solution** : Exécuter la Section 6 d'abord, puis revenir à la Section 5ter

#### Problème 3: `KeyError` avec des colonnes manquantes
**Cause** : Le dataset `df_enriched` ne contient pas les colonnes attendues  
**Solution** : Vérifier que les cellules de fusion des datasets (Section 2) et de feature engineering (Section 4) ont bien été exécutées

#### Problème 4: Performances anormalement basses (<0.4 en F1-Score)
**Cause** : Encodage ou standardisation mal appliqués  
**Solution** : Re-exécuter la Section 5bis depuis le début

---

## 📊 Analyse des Résultats

### A. Identifier le Data Leakage

**Calcul** :  
```python
diff_f1 = results_split_tardif['F1_Score'].mean() - results_split_precoce['F1_Score'].mean()
```

**Interprétation** :

| Différence (%) | Verdict | Action |
|----------------|---------|--------|
| > 3% | 🚨 Data Leakage CRITIQUE | Utiliser UNIQUEMENT split précoce |
| 1-3% | ⚠️ Data Leakage MODÉRÉ | Préférer split précoce |
| 0-1% | ✅ Leakage NÉGLIGEABLE | Split précoce par précaution |
| < 0% | ✅ Split Précoce MEILLEUR | Valider que c'est cohérent |

### B. Modèles les Plus Sensibles au Leakage

Les modèles les plus affectés par le data leakage sont généralement :
1. **k-NN** : Très sensible aux échelles et statistiques
2. **SVM** : Dépend fortement de la standardisation
3. **Régression Logistique** : Sensible aux statistiques d'imputation

Les modèles robustes (moins affectés) :
1. **Random Forest** : Gère bien les données brutes
2. **XGBoost** : Robuste aux différences de préparation
3. **Arbres de Décision** : Moins sensibles aux échelles

---

## 💡 Leçons Apprises

### 1. Le Timing du Split est CRUCIAL

**❌ MAUVAIS** :  
```
Données → Imputation → Encodage → Split → Standardisation → SMOTE
```
→ Data leakage aux étapes Imputation et Encodage

**✅ BON** :  
```
Données → Split → Imputation → Encodage → Standardisation → SMOTE
```
→ Aucun leakage

### 2. FIT vs TRANSFORM

**RÈGLE D'OR** :  
- **FIT** : Calculer les paramètres (moyenne, médiane, classes, etc.) sur le **train set UNIQUEMENT**
- **TRANSFORM** : Appliquer ces paramètres au **test set**

```python
# ✅ BON
imputer.fit(X_train)           # Calcule la médiane sur train
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)  # Utilise la médiane du train

# ❌ MAUVAIS
imputer.fit(X)                 # Calcule sur train + test
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)
```

### 3. SMOTE Uniquement sur Train

**POURQUOI** ? Le test set doit conserver sa distribution naturelle pour évaluer les performances en conditions réelles.

```python
# ✅ BON
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
# X_test reste inchangé

# ❌ MAUVAIS
X_smote, y_smote = smote.fit_resample(X, y)  # Sur tout le dataset
```

---

## 🎓 Pour Aller Plus Loin

### Questions à Explorer

1. **Quelle est la différence de performance entre split tardif et précoce pour chaque modèle ?**
   - Analyser `comparison_df['Diff_F1_Score']`
   
2. **Quel modèle est le plus robuste au data leakage ?**
   - Identifier celui avec la plus petite différence
   
3. **Comment évoluent les performances avec différents ratios de split ?**
   - Tester 70/30, 75/25, 85/15
   
4. **L'impact du leakage est-il plus important avec SMOTE ?**
   - Comparer avec et sans SMOTE

### Expérimentations Suggérées

#### Exp. 1: Changer le Ratio de Split
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3,  # Au lieu de 0.2
    random_state=42, 
    stratify=y
)
```

#### Exp. 2: Tester d'Autres Stratégies d'Imputation
```python
# Imputation par régression
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

imputer = IterativeImputer(random_state=42)
```

#### Exp. 3: Utiliser Pipeline de Sklearn
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)  # Tout est appliqué correctement
```

---

## 📝 Conclusion

### Acquis Méthodologiques

✅ Compréhension du **data leakage** et de son impact  
✅ Maîtrise du pipeline **fit/transform**  
✅ Application des **best practices ML**  
✅ Capacité à **comparer et valider** des approches  
✅ Esprit **critique et analytique** sur les résultats  

### Recommandation Finale

**TOUJOURS utiliser l'approche Split Précoce** dans vos projets :
1. C'est la norme de l'industrie
2. Évite les mauvaises surprises en production
3. Donne des estimations honnêtes et fiables
4. Démontre votre rigueur méthodologique

---

## 🔗 Ressources Complémentaires

### Articles et Tutoriels
- [Avoiding Data Leakage in ML](https://machinelearningmastery.com/data-leakage-machine-learning/)
- [Sklearn Pipeline Best Practices](https://scikit-learn.org/stable/modules/compose.html)
- [Cross-Validation Done Right](https://towardsdatascience.com/cross-validation-done-right-7c9c3c5f0e48)

### Documentation Sklearn
- [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
- [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)

---

**Date de création** : Février 2026  
**Version du notebook** : Employee_Attrition_Analysis.ipynb v2.0 (avec Section 5bis)  
**Auteur** : GitHub Copilot pour HumanForYou Analytics Team
