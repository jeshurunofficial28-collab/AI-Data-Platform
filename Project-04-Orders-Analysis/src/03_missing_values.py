import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Sales.csv
file_path = project_folder / "data" / "raw" / "Sales.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Check missing values
print(df.isnull().sum())

# Total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())