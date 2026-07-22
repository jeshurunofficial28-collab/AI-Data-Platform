from pathlib import Path

import joblib
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"
MODEL_PATH = PROJECT_DIR / "models" / "xgboost_model.pkl"

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# Feature Selection
# --------------------------------------------------

TARGET = "Revenue"

DROP_COLUMNS = [
    "Revenue",
    "Total Profit",
    "Profit",
    "Order Number",
    "Line Item",
    "CustomerKey",
    "StoreKey",
    "ProductKey",
    "Delivery Date",
    "Quantity",
    "Unit Price USD"
]

X = df.drop(columns=DROP_COLUMNS)
y = df[TARGET]

# --------------------------------------------------
# Encode Categorical Columns
# --------------------------------------------------

encoder = LabelEncoder()

categorical_columns = X.select_dtypes(include=["object", "string"]).columns

for column in categorical_columns:
    X[column] = encoder.fit_transform(X[column].astype(str))

# --------------------------------------------------
# Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# --------------------------------------------------
# Train Best Model (XGBoost)
# --------------------------------------------------

model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# --------------------------------------------------
# Save Model
# --------------------------------------------------

joblib.dump(model, MODEL_PATH)

print("=" * 60)
print("MODEL SAVED SUCCESSFULLY")
print("=" * 60)
print(f"Location : {MODEL_PATH}")