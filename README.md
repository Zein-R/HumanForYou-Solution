# Analyse Attrition - HumanForYou

Projet d'analyse prédictive de l'attrition des employés pour une entreprise pharmaceutique de 4000 employés en Inde.

---

## Documentation Complète

**[Documentation HumanForYou.md](Documentation%20HumanForYou.md)** - Documentation exhaustive (1100+ lignes)

Contient toutes les informations sur :
- Architecture et flux de données
- Méthodologie et justifications complètes
- Guides d'installation et d'utilisation
- Comparaison des approches (data leakage)
- Références et FAQ pour soutenance

---

## Démarrage Rapide (5 minutes)

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Lancer le notebook
jupyter notebook Employee_Attrition_Analysis.ipynb

# 3. Exécuter toutes les cellules
# Temps d'exécution : ~25-30 minutes
```

---

## Résultats Principaux

### Performances des Modèles

| Modèle | F1-Score | Recall | ROC-AUC |
|--------|----------|--------|---------|
| **Random Forest** (recommandé) | 0.76 | 0.78 | 0.90 |

### TOP 5 Facteurs d'Attrition

1. **WorkLifeBalance** - Équilibre vie pro/perso
2. **BusinessTravel** - Fréquence des déplacements
3. **YearsSinceLastPromotion** - Stagnation de carrière
4. **JobSatisfaction** - Satisfaction au travail
5. **DistanceFromHome** - Distance domicile-travail

### Impact Business

- **Réduction ciblée** : 15% → 10% en 24 mois
- **Économies estimées** : 12M€/an
- **ROI** : ×3 (investissement 3-4M€/an)

---

## Structure du Projet

```
HumanForYou Solution/
├── Employee_Attrition_Analysis.ipynb  # Notebook principal (4400+ lignes)
├── Documentation HumanForYou.md       # Documentation exhaustive
├── README.md                          # Ce fichier
├── requirements.txt                   # Dépendances Python
└── dataset/                           # 5 fichiers CSV (4410 lignes)
    ├── general_data.csv
    ├── manager_survey_data.csv
    ├── employee_survey_data.csv
    ├── in_time.csv
    └── out_time.csv
```

---

## Contexte

**Projet** : Machine Learning AI
**Date** : Février 2026  
**Méthodologie** : Split précoce (best practices ML + analyse comparative du data leakage)

---

Pour toute information détaillée, consultez [Documentation HumanForYou.md](Documentation%20HumanForYou.md).
