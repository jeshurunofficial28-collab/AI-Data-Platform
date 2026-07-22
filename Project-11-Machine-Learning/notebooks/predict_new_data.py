from pathlib import Path

import joblib
import pandas as pd

# --------------------------------------------------
# Load Saved Model
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "models" / "xgboost_model.pkl"

model = joblib.load(MODEL_PATH)

print("=" * 60)
print("MODEL LOADED SUCCESSFULLY")
print("=" * 60)

# --------------------------------------------------
# Create Sample Data
# --------------------------------------------------

sample = pd.DataFrame({
    "Order Date": [45000],
    "Currency Code": [0],
    "Large_Order": [1],
    "Product Name": [100],
    "Brand": [5],
    "Color": [2],
    "Unit Cost USD": [250],
    "SubcategoryKey": [12],
    "Subcategory": [8],
    "CategoryKey": [3],
    "Category": [1]
})

# --------------------------------------------------
# Prediction
# --------------------------------------------------

prediction = model.predict(sample)

print(f"\nPredicted Revenue: ${prediction[0]:.2f}")