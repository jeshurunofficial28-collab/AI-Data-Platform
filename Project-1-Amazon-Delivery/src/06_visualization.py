import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned dataset
df = pd.read_csv("data/processed/amazon_delivery_cleaned.csv")

# Count deliveries by vehicle
vehicle_count = df["Vehicle"].value_counts()

# Create bar chart
plt.figure(figsize=(8,5))
vehicle_count.plot(kind="bar")

plt.title("Number of Deliveries by Vehicle")
plt.xlabel("Vehicle")
plt.ylabel("Count")

plt.show()