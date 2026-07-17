import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Raw_Data.csv
file_path = project_folder / "data" / "raw" / "Raw_Data.csv"

# Read the dataset with UTF-8 BOM encoding
df = pd.read_csv(file_path, encoding="utf-8-sig")

# Display first 5 rows
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())