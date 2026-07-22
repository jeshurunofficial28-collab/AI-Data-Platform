import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ai_data_platform"
)

# Read all tables
customers_df = pd.read_sql("SELECT * FROM customers", connection)
products_df = pd.read_sql("SELECT * FROM products", connection)
orders_df = pd.read_sql("SELECT * FROM orders", connection)
shipment_df = pd.read_sql("SELECT * FROM shipment", connection)
amazon_df = pd.read_sql("SELECT * FROM amazon", connection)


# Function to display dataset overview
def data_overview(df, table_name):

    print("\n" + "=" * 60)
    print(f"{table_name.upper()} DATA OVERVIEW")
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nSummary Statistics:")
    print(df.describe(include="all"))


# Call the function for each table
data_overview(customers_df, "Customers")
data_overview(products_df, "Products")
data_overview(orders_df, "Orders")
data_overview(shipment_df, "Shipment")
data_overview(amazon_df, "Amazon")

# Close the connection
connection.close()