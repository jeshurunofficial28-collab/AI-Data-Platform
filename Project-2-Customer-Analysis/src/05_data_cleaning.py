import pandas as pd

# Read dataset
df = pd.read_csv("data/raw/customers.csv")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill numerical missing values
df["age"] = df["age"].fillna(df["age"].mean())

# Fill categorical missing values
df["preferred_channel"] = df["preferred_channel"].fillna(df["preferred_channel"].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())