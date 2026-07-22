import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Products.csv
file_path = project_folder / "data" / "Products.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Check for missing values
print("Missing Values:\n")
print(df.isnull().sum())

# Total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())