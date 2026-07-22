import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT = BASE_DIR / "output"

products = pd.read_csv(OUTPUT / "product_features.csv")

print(products[[
    "ProductKey",
    "Unit Cost USD",
    "Unit Price USD",
    "Profit"
]].head(20))

print("\nMissing Values:")
print(products[[
    "Unit Cost USD",
    "Unit Price USD",
    "Profit"
]].isnull().sum())