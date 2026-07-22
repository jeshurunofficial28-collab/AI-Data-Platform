from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

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
# Train Model
# --------------------------------------------------

model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# --------------------------------------------------
# Feature Importance
# --------------------------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)
print(importance)

# --------------------------------------------------
# Save CSV
# --------------------------------------------------

importance.to_csv(
    OUTPUT_DIR / "feature_importance.csv",
    index=False
)

# --------------------------------------------------
# Plot
# --------------------------------------------------

plt.figure(figsize=(10,6))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("XGBoost Feature Importance")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "feature_importance.png"
)

plt.show()
