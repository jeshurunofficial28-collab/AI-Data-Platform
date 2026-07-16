import pandas as pd

# Read the cleaned dataset
df = pd.read_csv("data/processed/amazon_delivery_cleaned.csv")

print("========== FINAL BUSINESS ANALYSIS ==========\n")

# Total Orders
print("Total Orders:", len(df))

# Average Delivery Time
print("\nAverage Delivery Time:")
print(df["Delivery_Time"].mean())

# Vehicle used the most
print("\nMost Used Vehicle:")
print(df["Vehicle"].value_counts().head())

# Most common Weather
print("\nWeather Distribution:")
print(df["Weather"].value_counts())

# Area Distribution
print("\nArea Distribution:")
print(df["Area"].value_counts())

# Top Categories
print("\nTop Categories:")
print(df["Category"].value_counts())