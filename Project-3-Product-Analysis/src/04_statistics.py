import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Products.csv
file_path = project_folder / "data" / "Products.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Display statistical summary
print("Statistical Summary:\n")
print(df.describe(include="all"))

# Number of unique brands
print("\nNumber of Unique Brands:")
print(df["Brand"].nunique())

# Number of unique categories
print("\nNumber of Unique Categories:")
print(df["Category"].nunique())

# Products by Category
print("\nProducts by Category:")
print(df["Category"].value_counts())

# Products by Brand
print("\nProducts by Brand:")
print(df["Brand"].value_counts())