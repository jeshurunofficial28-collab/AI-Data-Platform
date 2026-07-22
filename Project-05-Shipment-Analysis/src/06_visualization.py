import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read cleaned dataset
file_path = project_folder / "data" / "processed" / "Shipment_Cleaned.csv"
df = pd.read_csv(file_path)

# Convert date column
df["Scheduled Delivery Date"] = pd.to_datetime(df["Scheduled Delivery Date"])

# -----------------------------
# Chart 1 - Shipment Mode
# -----------------------------
df["Shipment Mode"].value_counts().plot(kind="bar")

plt.title("Shipment Mode Distribution")
plt.xlabel("Shipment Mode")
plt.ylabel("Number of Shipments")
plt.show()

# -----------------------------
# Chart 2 - Top 10 Countries
# -----------------------------
df["Country"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Destination Countries")
plt.xlabel("Country")
plt.ylabel("Number of Shipments")
plt.show()

# -----------------------------
# Chart 3 - Product Groups
# -----------------------------
df["Product Group"].value_counts().plot(kind="bar")

plt.title("Product Group Distribution")
plt.xlabel("Product Group")
plt.ylabel("Number of Shipments")
plt.show()

# -----------------------------
# Chart 4 - Monthly Shipments
# -----------------------------
monthly = df.groupby(
    df["Scheduled Delivery Date"].dt.to_period("M")
).size()

monthly.plot(kind="line")

plt.title("Monthly Shipments")
plt.xlabel("Month")
plt.ylabel("Number of Shipments")
plt.show()