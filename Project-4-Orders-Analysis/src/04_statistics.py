import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Sales.csv
file_path = project_folder / "data" / "raw" / "Sales.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Display statistics
print(df.describe(include="all"))

# Unique customers
print("\nUnique Customers:")
print(df["CustomerKey"].nunique())

# Unique products
print("\nUnique Products:")
print(df["ProductKey"].nunique())

# Unique stores
print("\nUnique Stores:")
print(df["StoreKey"].nunique())

# Currency distribution
print("\nCurrency Distribution:")
print(df["Currency Code"].value_counts())