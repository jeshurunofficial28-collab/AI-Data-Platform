import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data
response = requests.get(url)

if response.status_code == 200:

    # Convert JSON to Python
    data = response.json()

    # Convert Python data to DataFrame
    df = pd.DataFrame(data)

    print("✅ Data successfully converted to DataFrame!\n")

    # Display first 5 rows
    print(df.head())

    print("\n========================")

    # Display DataFrame information
    print(df.info())

else:
    print(f"Error: {response.status_code}")