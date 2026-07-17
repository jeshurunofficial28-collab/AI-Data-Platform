import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Products.csv
file_path = project_folder / "data" / "Products.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Remove '$' and ',' from currency columns
df["Unit Cost USD"] = (
    df["Unit Cost USD"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Unit Price USD"] = (
    df["Unit Price USD"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convert columns to numeric
df["Unit Cost USD"] = pd.to_numeric(df["Unit Cost USD"])
df["Unit Price USD"] = pd.to_numeric(df["Unit Price USD"])

# Check data types
print("Updated Data Types:\n")
print(df.dtypes)

# Save cleaned dataset
output_file = project_folder / "data" / "Products_Cleaned.csv"
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")