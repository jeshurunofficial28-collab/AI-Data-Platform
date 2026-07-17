import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to cleaned dataset
file_path = project_folder / "data" / "processed" / "Sales_Cleaned.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# -----------------------------
# Final Analysis
# -----------------------------

print("===== ORDERS ANALYSIS REPORT =====\n")

# Total Orders
print("Total Orders:", len(df))

# Unique Customers
print("Unique Customers:", df["CustomerKey"].nunique())

# Unique Products
print("Unique Products:", df["ProductKey"].nunique())

# Unique Stores
print("Unique Stores:", df["StoreKey"].nunique())

# Total Quantity Sold
print("Total Quantity Sold:", df["Quantity"].sum())

# Average Quantity
print("Average Quantity per Order:", round(df["Quantity"].mean(), 2))

# Currency Distribution
print("\nOrders by Currency:")
print(df["Currency Code"].value_counts())

# Top 10 Products
print("\nTop 10 Products:")
print(df["ProductKey"].value_counts().head(10))

# Monthly Orders
print("\nMonthly Orders:")
print(df.groupby(df["Order Date"].dt.to_period("M")).size())

print("\nOrders Analysis Completed Successfully!")