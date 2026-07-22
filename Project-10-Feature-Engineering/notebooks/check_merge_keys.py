import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT = BASE_DIR / "output"

orders = pd.read_csv(OUTPUT / "order_features.csv")
products = pd.read_csv(OUTPUT / "product_features.csv")

print("Orders ProductKey dtype:")
print(orders["ProductKey"].dtype)

print("\nProducts ProductKey dtype:")
print(products["ProductKey"].dtype)

print("\nOrders ProductKey sample:")
print(sorted(orders["ProductKey"].unique())[:20])

print("\nProducts ProductKey sample:")
print(sorted(products["ProductKey"].unique())[:20])

matched = orders["ProductKey"].isin(products["ProductKey"]).sum()

print(f"\nMatching ProductKeys: {matched} out of {len(orders)}")
