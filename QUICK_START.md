# 🚀 Guide de Démarrage Rapide

## ⚡ Installation en 5 minutes

### Option 1: Installation Complète (Recommandée)

```bash
# 1. Naviguer vers le dossier du projet
cd "BLOC VIII. IA Machine learning/HumanForYou Solution"

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement
# Sur Windows:
venv\Scripts\activate
# Sur Mac/Linux:
source venv/bin/activate

# 4. Installer toutes les dépendances
pip install -r requirements.txt

# 5. Lancer Jupyter Notebook
jupyter notebook
```

### Option 2: Installation Rapide (dans le notebook)

Si vous ne voulez pas créer d'environnement virtuel, ouvrez directement le notebook et exécutez la première cellule qui installe automatiquement tous les packages nécessaires.

---

## 📊 Exécution du Notebook

1. **Ouvrir le notebook**: `Employee_Attrition_Analysis.ipynb`

2. **Vérifier les données**: Assurez-vous que le dossier `dataset/` contient les 5 fichiers CSV:
   - ✅ general_data.csv
   - ✅ manager_survey_data.csv
   - ✅ employee_survey_data.csv
   - ✅ in_time.csv
   - ✅ out_time.csv

3. **Exécuter les cellules**: 
   - Option A: `Kernel > Restart & Run All` (exécuter tout)
   - Option B: `Shift + Enter` cellule par cellule

4. **Temps d'exécution**: ~10-15 minutes pour l'ensemble

---

## 🎯 Sections Principales du Notebook

| Section | Description | Durée estimée |
|---------|-------------|---------------|
| 1. Configuration | Installation et imports | 1 min |
| 2. Chargement des données | Lecture et fusion des CSV | 1 min |
| 3. EDA | Analyse exploratoire complète | 3 min |
| 4. Feature Engineering | Création de variables temporelles | 2 min |
| 5. Préparation | Nettoyage, encodage, normalisation | 1 min |
| 6. Modélisation | 7 algorithmes testés | 5 min |
| 7. Optimisation | GridSearchCV et validation croisée | 3 min |
| 8. Clustering | Segmentation des employés | 2 min |
| 9. Recommandations | Insights et actions business | Lecture |

---

## 📈 Résultats Attendus

Après exécution complète, vous obtiendrez:

✅ **30+ visualisations**:
- Distributions des variables
- Matrices de confusion
- Courbes ROC
- Feature importances
- Profils de clusters

✅ **Comparatif de 7 modèles**:
- Régression Logistique
- Arbre de Décision
- Random Forest
- SVM
- k-NN
- XGBoost
- LightGBM

✅ **TOP 5 facteurs d'attrition** identifiés

✅ **Plan d'action concret** avec ROI estimé à 12M€/an

---

## 🛠️ Dépannage

### Problème: Fichiers CSV non trouvés
```
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/general_data.csv'
```
**Solution**: Vérifiez que vous êtes dans le bon dossier et que `dataset/` est au bon endroit.

### Problème: Package manquant
```
ModuleNotFoundError: No module named 'xgboost'
```
**Solution**: 
```bash
pip install xgboost
# ou installer tous les packages:
pip install -r requirements.txt
```

### Problème: Mémoire insuffisante
**Solution**: 
- Fermer les autres applications
- Redémarrer le kernel Jupyter
- Réduire le nombre de modèles testés

### Problème: Exécution lente
**Solution**:
- La section GridSearchCV peut être longue (commentez-la si nécessaire)
- Réduire le nombre d'estimateurs dans Random Forest (de 100 à 50)

---

## 💡 Conseils d'Utilisation

### Pour une première exploration:
1. Exécutez sections 1-3 (Config + Chargement + EDA)
2. Lisez attentivement les insights de l'EDA
3. Passez directement à la section 9 (Recommandations)

### Pour une analyse approfondie:
1. Exécutez tout le notebook séquentiellement
2. Modifiez les paramètres des modèles
3. Testez d'autres techniques de feature engineering
4. Ajoutez vos propres analyses

### Pour une utilisation en production:
1. Extrayez le code dans des fichiers `.py` modulaires
2. Sauvegardez le meilleur modèle avec `joblib` ou `pickle`
3. Créez un pipeline de prédiction
4. Mettez en place un système de monitoring

---

## 📊 Données Exemples

### Structure de general_data.csv:
```
EmployeeID,Age,Attrition,BusinessTravel,Department,DistanceFromHome,...
1,41,Yes,Travel_Rarely,Sales,1,...
2,49,No,Travel_Frequently,Research,8,...
```

### Structure de in_time.csv:
```
EmployeeID,2015-01-01,2015-01-02,2015-01-03,...
1,2015-01-01 09:30:00,2015-01-02 09:15:00,...
```

---

## 🎓 Pour aller plus loin

### Modifications suggérées:
1. **Tester d'autres modèles**: LDA, QDA, Naive Bayes
2. **Deep Learning**: Réseau de neurones avec TensorFlow/Keras
3. **Analyse temporelle**: Prédiction mois par mois
4. **Feature selection**: Éliminer les variables redondantes
5. **Stacking/Ensemble**: Combiner plusieurs modèles

### Ressources complémentaires:
- 📚 [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- 📖 [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- 🎥 [Kaggle Learn](https://www.kaggle.com/learn) - Cours gratuits
- 📊 [Towards Data Science](https://towardsdatascience.com/) - Articles

---

## ✅ Checklist de Validation

Avant de considérer le projet comme terminé:

- [ ] Toutes les cellules s'exécutent sans erreur
- [ ] Les 5 datasets sont correctement fusionnés
- [ ] Les valeurs manquantes sont traitées
- [ ] Les 7 modèles ont des scores cohérents (ROC-AUC > 0.75)
- [ ] Les feature importances sont convergentes entre modèles
- [ ] Les recommandations sont documentées
- [ ] Le code est commenté et lisible
- [ ] Les visualisations sont claires

---

## 📧 Support

En cas de problème:
1. Vérifiez la section **Dépannage** ci-dessus
2. Consultez le fichier `README.md` pour plus de détails
3. Vérifiez les versions des packages dans `requirements.txt`

---

**Bon courage et bonne analyse ! 🚀**
