import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ai_data_platform"
)

# Read Customers table
customers_df = pd.read_sql("SELECT * FROM customers", connection)

print("=" * 50)
print("CUSTOMERS DATA OVERVIEW")
print("=" * 50)

# Shape
print("\nShape:")
print(customers_df.shape)

# Column Names
print("\nColumns:")
print(customers_df.columns)

# Data Types
print("\nData Types:")
print(customers_df.dtypes)

# Missing Values
print("\nMissing Values:")
print(customers_df.isnull().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(customers_df.describe(include="all"))

# Close connection
connection.close()