import pandas as pd

# Read dataset
df = pd.read_csv("data/raw/customers.csv")

# Dataset information
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nGeneral Info:")
print(df.info())