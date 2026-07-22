import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CLEAN = BASE_DIR / "data" / "clean"

customers = pd.read_csv(CLEAN / "customers_clean.csv")
orders = pd.read_csv(CLEAN / "orders_clean.csv")

print("Customers:")
print(customers["customer_id"].head(10))

print("\nOrders:")
print(orders["CustomerKey"].head(10))