# Project 11 - Machine Learning Revenue Prediction

## Overview

This project demonstrates an end-to-end Machine Learning workflow for predicting product revenue using historical sales data.

The project covers the complete ML lifecycle, including:

- Data Loading
- Data Understanding
- Feature Selection
- Data Preprocessing
- Train-Test Split
- Model Training
- Model Evaluation
- Feature Importance
- Model Saving
- Prediction using Saved Model

---

## Dataset

Source Dataset:

sales_master_dataset.csv

Records:
- 62,884 rows

Features Used:
- Order Date
- Currency Code
- Large_Order
- Product Name
- Brand
- Color
- Unit Cost USD
- SubcategoryKey
- Subcategory
- CategoryKey
- Category

Target Variable:

Revenue

---

## Machine Learning Models

The following regression models were trained and evaluated:

1. Linear Regression
2. Random Forest
3. XGBoost
4. LightGBM
5. CatBoost

---

## Model Performance

| Model | MAE | RMSE | R² Score |
|------|------:|------:|------:|
| XGBoost | 214.23 | 383.64 | 0.8635 |
| LightGBM | 215.34 | 384.44 | 0.8629 |
| CatBoost | 222.13 | 392.59 | 0.8570 |
| Random Forest | 228.16 | 411.31 | 0.8431 |
| Linear Regression | 305.72 | 525.59 | 0.7437 |

---

## Best Model

XGBoost achieved the highest performance.

- Lowest MAE
- Lowest RMSE
- Highest R² Score

Final R² Score:

0.8635

---

## Feature Importance

The most influential features were:

1. Large_Order
2. Unit Cost USD
3. SubcategoryKey
4. Subcategory
5. Product Name

Feature importance visualization is available in:

output/feature_importance.png

---

## Project Structure

```
Project-11-Machine-Learning/

├── data/
├── models/
├── notebooks/
├── output/
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- XGBoost
- LightGBM
- CatBoost
- Joblib

---

## Key Learning Outcomes

- Machine Learning workflow
- Regression algorithms
- Feature Engineering
- Label Encoding
- Model Evaluation
- Feature Importance
- Target Leakage Detection
- Model Serialization
- Revenue Prediction

---

## Business Conclusion

Tree-based ensemble models significantly outperformed Linear Regression for revenue prediction.

Among all models, XGBoost produced the best balance of accuracy and generalization, making it the preferred model for deployment.

---



