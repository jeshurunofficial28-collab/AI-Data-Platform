import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Sales.csv
file_path = project_folder / "data" / "raw" / "Sales.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Delivery Date"] = pd.to_datetime(df["Delivery Date"])

# Save the cleaned dataset
output_file = project_folder / "data" / "processed" / "Sales_Cleaned.csv"
df.to_csv(output_file, index=False)

# Display updated data types
print(df.dtypes)

print("\nData Cleaning Completed Successfully!")