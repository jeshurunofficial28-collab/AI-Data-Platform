from pathlib import Path
import pandas as pd

# Project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("FEATURE SELECTION")
print("=" * 60)

# -------------------------------------------------
# Target Variable
# -------------------------------------------------
TARGET = "Revenue"

print(f"\nTarget Variable: {TARGET}")

# -------------------------------------------------
# Columns to Drop
# -------------------------------------------------
DROP_COLUMNS = [
    "Revenue",          # Target
    "Total Profit",     # Derived from Revenue
    "Profit",           # Derived feature
    "Order Number",     # Identifier
    "Line Item",        # Identifier
    "CustomerKey",      # Identifier
    "StoreKey",         # Identifier
    "ProductKey",       # Identifier
    "Delivery Date"     # Too many missing values
]

# Features
X = df.drop(columns=DROP_COLUMNS)

# Target
y = df[TARGET]

print("\nSelected Features:")
for column in X.columns:
    print(f"- {column}")

print(f"\nNumber of Features : {X.shape[1]}")
print(f"Target Shape       : {y.shape}")

print("\nFeature Selection Completed Successfully!")