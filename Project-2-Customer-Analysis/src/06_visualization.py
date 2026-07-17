import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("data/raw/customers.csv")

# Fill missing values for visualization
df["age"] = df["age"].fillna(df["age"].mean())
df["preferred_channel"] = df["preferred_channel"].fillna(df["preferred_channel"].mode()[0])

# Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df["age"], bins=10)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# Gender Distribution
plt.figure(figsize=(6,4))
df["gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Preferred Channel
plt.figure(figsize=(6,4))
df["preferred_channel"].value_counts().plot(kind="bar")
plt.title("Preferred Shopping Channel")
plt.xlabel("Channel")
plt.ylabel("Customers")
plt.show()