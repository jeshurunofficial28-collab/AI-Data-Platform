import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT = BASE_DIR / "output"

sales = pd.read_csv(OUTPUT / "sales_master_dataset.csv")

print("=" * 60)
print("DATA VALIDATION REPORT")
print("=" * 60)

print("\nDuplicate Rows:")
print(sales.duplicated().sum())

print("\nMissing Values:")
print(sales.isnull().sum())

print("\nNegative Revenue:")
print((sales["Revenue"] < 0).sum())

print("\nNegative Profit:")
print((sales["Total Profit"] < 0).sum())

print("\nDataset Shape:")
print(sales.shape)

print("\nValidation Completed Successfully!")