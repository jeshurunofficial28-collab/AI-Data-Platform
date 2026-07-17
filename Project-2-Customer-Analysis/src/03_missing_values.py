import pandas as pd

# Read dataset
df = pd.read_csv("data/raw/customers.csv")

# Check missing values
print(df.isnull().sum())