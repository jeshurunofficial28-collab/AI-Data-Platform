import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ai_data_platform"
)

# Read each table into a Pandas DataFrame
customers_df = pd.read_sql("SELECT * FROM customers", connection)
products_df = pd.read_sql("SELECT * FROM products", connection)
orders_df = pd.read_sql("SELECT * FROM orders", connection)
shipment_df = pd.read_sql("SELECT * FROM shipment", connection)
amazon_df = pd.read_sql("SELECT * FROM amazon", connection)

# Display first 5 rows of each table
print("\n===== CUSTOMERS =====")
print(customers_df.head())

print("\n===== PRODUCTS =====")
print(products_df.head())

print("\n===== ORDERS =====")
print(orders_df.head())

print("\n===== SHIPMENT =====")
print(shipment_df.head())

print("\n===== AMAZON =====")
print(amazon_df.head())

# Close the connection
connection.close()