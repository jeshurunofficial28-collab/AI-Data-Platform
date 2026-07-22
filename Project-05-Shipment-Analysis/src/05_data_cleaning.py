import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path
file_path = project_folder / "data" / "raw" / "Raw_Data.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Rename the first column
df.rename(columns={"Ã¯Â»Â¿ID": "ID"}, inplace=True)

# Drop unnecessary columns
df.drop(columns=["Load_Date", "Source_System"], inplace=True)

# Convert date columns
date_columns = [
    "PQ First Sent to Client Date",
    "PO Sent to Vendor Date",
    "Scheduled Delivery Date",
    "Delivered to Client Date",
    "Delivery Recorded Date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Save cleaned dataset
output_file = project_folder / "data" / "processed" / "Shipment_Cleaned.csv"

df.to_csv(output_file, index=False)

print(df.dtypes)

print("\nData Cleaning Completed Successfully!")