import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

datasets = {
    "Amazon": pd.read_csv(DATA_DIR / "amazon_delivery.csv"),
    "Customers": pd.read_csv(DATA_DIR / "customers.csv"),
    "Products": pd.read_csv(DATA_DIR / "Products.csv"),
    "Orders": pd.read_csv(DATA_DIR / "Sales.csv"),
    "Shipment": pd.read_csv(DATA_DIR / "Raw_Data.csv"),
}

for name, df in datasets.items():
    print("\n" + "=" * 70)
    print(name.upper())
    print("=" * 70)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())