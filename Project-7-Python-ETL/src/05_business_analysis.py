import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ai_data_platform"
)

# Read tables
customers_df = pd.read_sql("SELECT * FROM customers", connection)
products_df = pd.read_sql("SELECT * FROM products", connection)
orders_df = pd.read_sql("SELECT * FROM orders", connection)
shipment_df = pd.read_sql("SELECT * FROM shipment", connection)
amazon_df = pd.read_sql("SELECT * FROM amazon", connection)

# -----------------------------
# CUSTOMER ANALYSIS
# -----------------------------
print("\n========== CUSTOMER ANALYSIS ==========")

print("\nCustomers by Gender")
print(customers_df["gender"].value_counts())

print("\nAverage Age")
print(customers_df["age"].mean())

# -----------------------------
# PRODUCT ANALYSIS
# -----------------------------
print("\n========== PRODUCT ANALYSIS ==========")

print("\nProducts by Category")
print(products_df["Category"].value_counts())

# -----------------------------
# ORDERS ANALYSIS
# -----------------------------
print("\n========== ORDERS ANALYSIS ==========")

print("\nOrders by Currency")
print(orders_df["Currency Code"].value_counts())

# -----------------------------
# SHIPMENT ANALYSIS
# -----------------------------
print("\n========== SHIPMENT ANALYSIS ==========")

print("\nShipment Mode")
print(shipment_df["Shipment Mode"].value_counts())

# -----------------------------
# AMAZON ANALYSIS
# -----------------------------
print("\n========== AMAZON ANALYSIS ==========")

print("\nAverage Delivery Time by Weather")
print(
    amazon_df.groupby("Weather")["Delivery_Time"].mean().round(2)
)

# Close connection
connection.close()