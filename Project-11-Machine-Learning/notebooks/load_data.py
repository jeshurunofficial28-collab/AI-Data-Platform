from pathlib import Path
import pandas as pd

# Get the project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Build the dataset path
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("=" * 50)
print("Sales Master Dataset Loaded Successfully")
print("=" * 50)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())