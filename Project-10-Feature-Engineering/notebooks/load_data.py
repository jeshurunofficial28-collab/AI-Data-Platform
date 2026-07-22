import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

amazon = pd.read_csv(DATA_DIR / "raw" / "amazon_delivery.csv")
customers = pd.read_csv(DATA_DIR / "raw" / "customers.csv")
products = pd.read_csv(DATA_DIR / "raw" / "Products.csv")
orders = pd.read_csv(DATA_DIR / "raw" / "Sales.csv")
shipment = pd.read_csv(DATA_DIR / "raw" / "Raw_Data.csv")

datasets = {
    "Amazon Delivery": amazon,
    "Customers": customers,
    "Products": products,
    "Orders": orders,
    "Shipment": shipment
}

for name, df in datasets.items():
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)
    print("Shape:", df.shape)
    print(df.head(3))