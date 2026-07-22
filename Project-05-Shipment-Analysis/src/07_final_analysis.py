import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the cleaned dataset
file_path = project_folder / "data" / "processed" / "Shipment_Cleaned.csv"

df = pd.read_csv(file_path)

# Convert date column
df["Scheduled Delivery Date"] = pd.to_datetime(
    df["Scheduled Delivery Date"],
    errors="coerce"
)

print("=" * 50)
print("SHIPMENT ANALYSIS REPORT")
print("=" * 50)

# Dataset Summary
print(f"\nTotal Shipments: {len(df)}")
print(f"Total Countries: {df['Country'].nunique()}")
print(f"Total Vendors: {df['Vendor'].nunique()}")
print(f"Total Project Codes: {df['Project Code'].nunique()}")

# Shipment Mode
print("\nShipment Mode Distribution:")
print(df["Shipment Mode"].value_counts())

# Product Groups
print("\nProduct Group Distribution:")
print(df["Product Group"].value_counts())

# Top 10 Countries
print("\nTop 10 Destination Countries:")
print(df["Country"].value_counts().head(10))

# Top 10 Vendors
print("\nTop 10 Vendors:")
print(df["Vendor"].value_counts().head(10))

# Shipment Trend
print("\nMonthly Shipments:")
print(df.groupby(df["Scheduled Delivery Date"].dt.to_period("M")).size())

# Financial Summary
print("\nFinancial Summary")

print(f"Total Line Item Value: ${df['Line Item Value'].sum():,.2f}")
print(f"Average Line Item Value: ${df['Line Item Value'].mean():,.2f}")

print(f"\nAverage Pack Price: ${df['Pack Price'].mean():,.2f}")
print(f"Average Unit Price: ${df['Unit Price'].mean():,.2f}")

print("\nShipment Analysis Completed Successfully!")