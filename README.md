# Attrition Analysis - HumanForYou

Predictive analysis project on employee attrition for a pharmaceutical company of 4,000 employees in India.

---

## Full Documentation

**[Documentation HumanForYou.md](Documentation%20HumanForYou.md)** - Exhaustive documentation (1100+ lines)

Contains all the details on:
- Architecture and data flow
- Methodology and full justifications
- Installation and usage guides
- Comparison of approaches (data leakage)
- References and FAQ for the project defense

---

## Quick Start (5 minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the notebook
jupyter notebook Employee_Attrition_Analysis.ipynb

# 3. Run all cells
# Execution time: ~25-30 minutes
```

---

## Key Results

### Model Performance

| Model | F1-Score | Recall | ROC-AUC |
|--------|----------|--------|---------|
| **Random Forest** (recommended) | 0.76 | 0.78 | 0.90 |

### Top 5 Attrition Drivers

1. **WorkLifeBalance** - Work/life balance
2. **BusinessTravel** - Frequency of business travel
3. **YearsSinceLastPromotion** - Career stagnation
4. **JobSatisfaction** - Job satisfaction
5. **DistanceFromHome** - Distance between home and workplace

### Business Impact

- **Targeted reduction**: 15% → 10% over 24 months
- **Estimated savings**: €12M/year
- **ROI**: ×3 (€3-4M/year investment)

---

## Project Structure

```
HumanForYou Solution/
├── Employee_Attrition_Analysis.ipynb  # Main notebook (4400+ lines)
├── Documentation HumanForYou.md       # Full documentation
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
└── dataset/                           # 5 CSV files (4410 rows)
    ├── general_data.csv
    ├── manager_survey_data.csv
    ├── employee_survey_data.csv
    ├── in_time.csv
    └── out_time.csv
```

## Data

| File | Description | Rows | Variables |
|---------|-------------|--------|-----------|
| `general_data.csv` | Demographic and professional data | 4410 | 26 |
| `manager_survey_data.csv` | Manager evaluations (February 2015) | 4410 | 3 |
| `employee_survey_data.csv` | Satisfaction survey (June 2015) | 4410 | 4 |
| `in_time.csv` | 2015 clock-in times | 4000 | 262 |
| `out_time.csv` | 2015 clock-out times | 4000 | 262 |

Target variable: **Attrition** (Yes/No) — whether the employee left the company in 2016.

## Tech stack

- Python (Jupyter notebook)
- pandas, numpy for data handling
- matplotlib, seaborn, plotly for visualization
- scikit-learn, imbalanced-learn, xgboost, lightgbm for modeling
- statsmodels, scipy for statistics

See `requirements.txt` for exact package versions.

## Context

**Project**: AI & Machine Learning
**Date**: February 2026
**Authors**: Zein, Saheen, Téo, Noan
**Methodology**: early split (ML best practices + comparative analysis of data leakage)

---

For detailed information, see [Documentation HumanForYou.md](Documentation%20HumanForYou.md).
