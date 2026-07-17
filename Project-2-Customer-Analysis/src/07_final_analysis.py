import pandas as pd

# Read dataset
df = pd.read_csv("data/raw/customers.csv")

# Clean missing values
df["age"] = df["age"].fillna(df["age"].mean())
df["preferred_channel"] = df["preferred_channel"].fillna(df["preferred_channel"].mode()[0])

print("========== CUSTOMER DATA ANALYSIS ==========\n")

print("Total Customers:")
print(len(df))

print("\nAverage Age:")
print(round(df["age"].mean(), 2))

print("\nGender Distribution:")
print(df["gender"].value_counts())

print("\nPreferred Shopping Channel:")
print(df["preferred_channel"].value_counts())

print("\nTop 10 States:")
print(df["state"].value_counts().head(10))