import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Raw_Data.csv
file_path = project_folder / "data" / "raw" / "Raw_Data.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Display missing values
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())