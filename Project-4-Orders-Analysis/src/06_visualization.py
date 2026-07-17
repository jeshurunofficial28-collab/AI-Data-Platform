import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Build the path to cleaned dataset
file_path = project_folder / "data" / "processed" / "Sales_Cleaned.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# -----------------------------
# Chart 1 - Orders by Currency
# -----------------------------
df["Currency Code"].value_counts().plot(kind="bar")

plt.title("Orders by Currency")
plt.xlabel("Currency")
plt.ylabel("Number of Orders")
plt.show()

# -----------------------------
# Chart 2 - Quantity Distribution
# -----------------------------
plt.hist(df["Quantity"], bins=10)

plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# Chart 3 - Monthly Orders
# -----------------------------
monthly_orders = df.groupby(df["Order Date"].dt.to_period("M")).size()

monthly_orders.plot(kind="line")

plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.show()
