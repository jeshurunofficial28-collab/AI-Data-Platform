import pandas as pd
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Products.csv
file_path = project_folder / "data" / "raw" / "Products.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Display the first 5 rows
print(df.head())