import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data
response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    df = pd.DataFrame(data)

    # Export to CSV
    df.to_csv("Project-9-REST-API/output/users.csv", index=False)

    print("✅ Data exported successfully!")
    print("File saved as: output/users.csv")

else:
    print(f"Error: {response.status_code}")