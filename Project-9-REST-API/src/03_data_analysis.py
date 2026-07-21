import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data
response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    df = pd.DataFrame(data)

    print("=== First 5 Rows ===")
    print(df.head())

    print("\n=== Data Shape ===")
    print(df.shape)

    print("\n=== Column Names ===")
    print(df.columns)

    print("\n=== User Names ===")
    print(df["name"])

    print("\n=== Email Addresses ===")
    print(df["email"])

else:
    print(f"Error: {response.status_code}")