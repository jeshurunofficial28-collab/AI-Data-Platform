import pandas as pd
from pathlib import Path

# ======================================
# Paths
# ======================================
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT = BASE_DIR / "output"

# ======================================
# Load Feature Engineered Data
# ======================================
orders = pd.read_csv(OUTPUT / "order_features.csv")
products = pd.read_csv(OUTPUT / "product_features.csv")

# ======================================
# Merge Orders + Products
# ======================================
sales = pd.merge(
    orders,
    products,
    on="ProductKey",
    how="left"
)

# ======================================
# Fill Missing Financial Values
# ======================================
sales["Unit Cost USD"] = sales["Unit Cost USD"].fillna(0)
sales["Unit Price USD"] = sales["Unit Price USD"].fillna(0)
sales["Profit"] = sales["Profit"].fillna(0)

# ======================================
# Create Revenue
# ======================================
sales["Revenue"] = (
    sales["Quantity"] * sales["Unit Price USD"]
)

# ======================================
# Create Total Profit
# ======================================
sales["Total Profit"] = (
    sales["Quantity"] * sales["Profit"]
)

# ======================================
# Save Final Dataset
# ======================================
sales.to_csv(
    OUTPUT / "sales_master_dataset.csv",
    index=False
)

# ======================================
# Summary
# ======================================
print("=" * 60)
print("SALES MASTER DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"Rows    : {sales.shape[0]}")
print(f"Columns : {sales.shape[1]}")

print("\nMissing Financial Values:")
print(sales[[
    "Unit Cost USD",
    "Unit Price USD",
    "Profit",
    "Revenue",
    "Total Profit"
]].isnull().sum())

print("\nTotal Revenue:")
print(f"${sales['Revenue'].sum():,.2f}")

print("\nTotal Profit:")
print(f"${sales['Total Profit'].sum():,.2f}")

print("\nDataset saved to:")
print(OUTPUT / "sales_master_dataset.csv")