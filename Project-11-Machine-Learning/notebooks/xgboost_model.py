from pathlib import Path

import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"

df = pd.read_csv(DATA_PATH)

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

encoder = LabelEncoder()

categorical_columns = X.select_dtypes(include=["object", "string"]).columns

for column in categorical_columns:
    X[column] = encoder.fit_transform(X[column].astype(str))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
)

model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("=" * 60)
print("XGBOOST RESULTS")
print("=" * 60)

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")