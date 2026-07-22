import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Raw_Data.csv
file_path = project_folder / "data" / "raw" / "Raw_Data.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Display descriptive statistics
print(df.describe(include="all"))

# Unique Countries
print("\nUnique Countries:")
print(df["Country"].nunique())

# Unique Vendors
print("\nUnique Vendors:")
print(df["Vendor"].nunique())

# Shipment Modes
print("\nShipment Modes:")
print(df["Shipment Mode"].value_counts())

# Product Groups
print("\nProduct Groups:")
print(df["Product Group"].value_counts())