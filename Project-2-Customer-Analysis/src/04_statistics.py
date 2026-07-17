import pandas as pd

# Read dataset
df = pd.read_csv("data/raw/customers.csv")

# Statistics
print(df.describe())