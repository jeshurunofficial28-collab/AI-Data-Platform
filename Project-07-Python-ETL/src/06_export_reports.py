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
# Customer Report
# -----------------------------
customer_summary = customers_df["gender"].value_counts().reset_index()
customer_summary.columns = ["Gender", "Count"]

# -----------------------------
# Product Report
# -----------------------------
product_summary = products_df["Category"].value_counts().reset_index()
product_summary.columns = ["Category", "Count"]

# -----------------------------
# Orders Report
# -----------------------------
orders_summary = orders_df["Currency Code"].value_counts().reset_index()
orders_summary.columns = ["Currency", "Orders"]

# -----------------------------
# Shipment Report
# -----------------------------
shipment_summary = shipment_df["Shipment Mode"].value_counts().reset_index()
shipment_summary.columns = ["Shipment Mode", "Count"]

# -----------------------------
# Amazon Report
# -----------------------------
amazon_summary = (
    amazon_df.groupby("Weather")["Delivery_Time"]
    .mean()
    .round(2)
    .reset_index()
)

# Export CSV files
customer_summary.to_csv("Project-7-Python-ETL/output/customer_summary.csv", index=False)
product_summary.to_csv("Project-7-Python-ETL/output/product_summary.csv", index=False)
orders_summary.to_csv("Project-7-Python-ETL/output/orders_summary.csv", index=False)
shipment_summary.to_csv("Project-7-Python-ETL/output/shipment_summary.csv", index=False)
amazon_summary.to_csv("Project-7-Python-ETL/output/amazon_summary.csv", index=False)

print("✅ Reports exported successfully!")

# Close connection
connection.close()