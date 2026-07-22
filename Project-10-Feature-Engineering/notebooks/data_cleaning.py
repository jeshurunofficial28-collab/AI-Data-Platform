import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW = BASE_DIR / "data" / "raw"
CLEAN = BASE_DIR / "data" / "clean"

CLEAN.mkdir(exist_ok=True)

amazon = pd.read_csv(RAW / "amazon_delivery.csv")
customers = pd.read_csv(RAW / "customers.csv")
products = pd.read_csv(RAW / "Products.csv")
orders = pd.read_csv(RAW / "Sales.csv")
shipment = pd.read_csv(RAW / "Raw_Data.csv", encoding="latin1")

# Remove duplicates
amazon = amazon.drop_duplicates()
customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()
shipment = shipment.drop_duplicates()

# Fill missing values
amazon["Agent_Rating"] = amazon["Agent_Rating"].fillna(amazon["Agent_Rating"].median())
amazon["Weather"] = amazon["Weather"].fillna("Unknown")

customers = customers.fillna("Unknown")

shipment["Shipment Mode"] = shipment["Shipment Mode"].fillna("Unknown")
shipment["Dosage"] = shipment["Dosage"].fillna("Unknown")
shipment["Line Item Insurance (USD)"] = shipment["Line Item Insurance (USD)"].fillna("0")
shipment["Load_Date"] = shipment["Load_Date"].fillna("Unknown")
shipment["Source_System"] = shipment["Source_System"].fillna("Unknown")

# Save cleaned files
amazon.to_csv(CLEAN / "amazon_delivery_clean.csv", index=False)
customers.to_csv(CLEAN / "customers_clean.csv", index=False)
products.to_csv(CLEAN / "products_clean.csv", index=False)
orders.to_csv(CLEAN / "orders_clean.csv", index=False)
shipment.to_csv(CLEAN / "shipment_clean.csv", index=False)

print("✅ Data Cleaning Completed Successfully!")