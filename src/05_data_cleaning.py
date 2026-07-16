import pandas as pd

# Read the dataset
df = pd.read_csv("data/raw/amazon_delivery.csv")

# Check missing values before cleaning
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values
df["Agent_Rating"] = df["Agent_Rating"].fillna(df["Agent_Rating"].mean())
df["Weather"] = df["Weather"].fillna("Unknown")

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("data/processed/amazon_delivery_cleaned.csv", index=False)

print("\n Cleaned dataset saved successfully!")