import pandas as pd

# Read the dataset
df = pd.read_csv("data/raw/amazon_delivery.csv")

# Show missing values
print(df.isnull().sum())