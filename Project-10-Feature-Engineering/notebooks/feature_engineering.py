import pandas as pd
from pathlib import Path

# ======================================
# Paths
# ======================================
BASE_DIR = Path(__file__).resolve().parent.parent
CLEAN = BASE_DIR / "data" / "clean"
OUTPUT = BASE_DIR / "output"

OUTPUT.mkdir(exist_ok=True)

# ======================================
# Load Cleaned Data
# ======================================
amazon = pd.read_csv(CLEAN / "amazon_delivery_clean.csv")
customers = pd.read_csv(CLEAN / "customers_clean.csv")
products = pd.read_csv(CLEAN / "products_clean.csv")
orders = pd.read_csv(CLEAN / "orders_clean.csv")
shipment = pd.read_csv(CLEAN / "shipment_clean.csv")

# ======================================
# AMAZON FEATURES
# ======================================
amazon["Fast_Delivery"] = (amazon["Delivery_Time"] <= 30).astype(int)
amazon["High_Rated_Agent"] = (amazon["Agent_Rating"] >= 4.5).astype(int)

# ======================================
# CUSTOMER FEATURES
# ======================================
customers["age"] = pd.to_numeric(customers["age"], errors="coerce")
customers["age"] = customers["age"].fillna(customers["age"].median())

customers["Age_Group"] = pd.cut(
    customers["age"],
    bins=[0, 18, 30, 45, 60, 100],
    labels=["Teen", "Young", "Adult", "Senior", "Old"],
    include_lowest=True
)

# ======================================
# PRODUCT FEATURES
# ======================================

# Remove $ and spaces
products["Unit Cost USD"] = (
    products["Unit Cost USD"]
    .str.replace("$", "", regex=False)
    .str.strip()
)

products["Unit Price USD"] = (
    products["Unit Price USD"]
    .str.replace("$", "", regex=False)
    .str.strip()
)

# Convert to numeric
products["Unit Cost USD"] = pd.to_numeric(
    products["Unit Cost USD"],
    errors="coerce"
)

products["Unit Price USD"] = pd.to_numeric(
    products["Unit Price USD"],
    errors="coerce"
)

# Profit
products["Profit"] = (
    products["Unit Price USD"]
    - products["Unit Cost USD"]
)

# ======================================
# ORDER FEATURES
# ======================================
orders["Large_Order"] = (orders["Quantity"] >= 5).astype(int)

# ======================================
# SHIPMENT FEATURES
# ======================================
shipment["Line Item Value"] = pd.to_numeric(
    shipment["Line Item Value"],
    errors="coerce"
)

shipment["High_Value_Shipment"] = (
    shipment["Line Item Value"] >= 10000
).astype(int)

# ======================================
# SAVE
# ======================================
amazon.to_csv(OUTPUT / "amazon_features.csv", index=False)
customers.to_csv(OUTPUT / "customer_features.csv", index=False)
products.to_csv(OUTPUT / "product_features.csv", index=False)
orders.to_csv(OUTPUT / "order_features.csv", index=False)
shipment.to_csv(OUTPUT / "shipment_features.csv", index=False)

print("=" * 60)
print("✅ FEATURE ENGINEERING COMPLETED")
print("=" * 60)