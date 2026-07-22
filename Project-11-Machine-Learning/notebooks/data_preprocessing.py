from pathlib import Path
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Target
TARGET = "Revenue"

# Drop unwanted columns
DROP_COLUMNS = [
    "Revenue",
    "Total Profit",
    "Profit",
    "Order Number",
    "Line Item",
    "CustomerKey",
    "StoreKey",
    "ProductKey",
    "Delivery Date"
]

X = df.drop(columns=DROP_COLUMNS)
y = df[TARGET]

print("=" * 60)
print("DATA PREPROCESSING")
print("=" * 60)

# Find categorical columns
categorical_columns = X.select_dtypes(include=["object", "string"]).columns

print("\nCategorical Columns:")
print(list(categorical_columns))

# Label Encoding
encoder = LabelEncoder()

for column in categorical_columns:
    X[column] = encoder.fit_transform(X[column].astype(str))

print("\nEncoded Successfully!")

print("\nFirst 5 Rows:")
print(X.head())

print("\nShape of Features :", X.shape)
print("Shape of Target   :", y.shape)