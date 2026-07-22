import pandas as pd
from pathlib import Path

# ===========================
# Paths
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT = BASE_DIR / "output"

sales = pd.read_csv(OUTPUT / "sales_master_dataset.csv")

print("=" * 60)
print("SALES MASTER DATASET SUMMARY")
print("=" * 60)

print("\nShape:")
print(sales.shape)

print("\nData Types:")
print(sales.dtypes)

print("\nMissing Values:")
print(sales.isnull().sum())

print("\nSummary Statistics:")
print(sales.describe())

print("\nTop 10 Product Categories:")
print(sales["Category"].value_counts().head(10))

print("\nTop 10 Brands:")
print(sales["Brand"].value_counts().head(10))

print("\nTotal Revenue:")
print(f"${sales['Revenue'].sum():,.2f}")

print("\nTotal Profit:")
print(f"${sales['Total Profit'].sum():,.2f}")

print("\nAverage Order Quantity:")
print(round(sales["Quantity"].mean(), 2))