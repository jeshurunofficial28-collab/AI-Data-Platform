from pathlib import Path
import pandas as pd

# Project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DATA UNDERSTANDING")
print("=" * 60)

# Dataset Shape
print("\n1. Dataset Shape")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# Column Names
print("\n2. Column Names")
for col in df.columns:
    print(f"- {col}")

# Data Types
print("\n3. Data Types")
print(df.dtypes)

# Missing Values
print("\n4. Missing Values")
print(df.isnull().sum())

# Duplicate Records
print("\n5. Duplicate Records")
print(df.duplicated().sum())

# Numerical Columns
print("\n6. Numerical Columns")
print(df.select_dtypes(include=["int64", "float64"]).columns.tolist())

# Categorical Columns
print("\n7. Categorical Columns")
print(df.select_dtypes(include=["object"]).columns.tolist())

# Summary Statistics
print("\n8. Summary Statistics")
print(df.describe())

print("\nDataset Understanding Completed Successfully!")