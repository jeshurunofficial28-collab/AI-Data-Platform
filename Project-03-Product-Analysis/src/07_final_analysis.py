import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Products_Cleaned.csv
file_path = project_folder / "data" / "Products_Cleaned.csv"

# Read the cleaned dataset
df = pd.read_csv(file_path)

# Total Products
print("Total Products:")
print(len(df))

# Unique Brands
print("\nUnique Brands:")
print(df["Brand"].nunique())

# Unique Categories
print("\nUnique Categories:")
print(df["Category"].nunique())

# Average Unit Cost
print("\nAverage Unit Cost (USD):")
print(round(df["Unit Cost USD"].mean(), 2))

# Average Unit Price
print("\nAverage Unit Price (USD):")
print(round(df["Unit Price USD"].mean(), 2))

# Most Common Category
print("\nMost Common Category:")
print(df["Category"].value_counts().head())

# Top Brands
print("\nTop 10 Brands:")
print(df["Brand"].value_counts().head(10))

# Most Expensive Products
print("\nTop 10 Most Expensive Products:")
print(
    df[["Product Name", "Unit Price USD"]]
    .sort_values(by="Unit Price USD", ascending=False)
    .head(10)
)

# Cheapest Products
print("\nTop 10 Cheapest Products:")
print(
    df[["Product Name", "Unit Price USD"]]
    .sort_values(by="Unit Price USD", ascending=True)
    .head(10)
)

print("\nProduct Analysis Completed Successfully!")