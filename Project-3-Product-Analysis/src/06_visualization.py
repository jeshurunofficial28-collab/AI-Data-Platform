import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to Products_Cleaned.csv
file_path = project_folder / "data" / "Products_Cleaned.csv"

# Read the cleaned dataset
df = pd.read_csv(file_path)

# -----------------------------
# Products by Category
# -----------------------------
category_counts = df["Category"].value_counts()

plt.figure(figsize=(10,6))
category_counts.plot(kind="bar")
plt.title("Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Products by Brand
# -----------------------------
brand_counts = df["Brand"].value_counts()

plt.figure(figsize=(10,6))
brand_counts.plot(kind="bar")
plt.title("Products by Brand")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Unit Price Distribution
# -----------------------------
plt.figure(figsize=(10,6))
plt.hist(df["Unit Price USD"], bins=20)
plt.title("Unit Price Distribution")
plt.xlabel("Unit Price (USD)")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.show()