import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check request status
if response.status_code == 200:
    print("✅ API Request Successful!\n")

    # Convert JSON response to Python
    data = response.json()

    # Print all user data
    for user in data:
        print(user)

else:
    print(f"❌ Error: {response.status_code}")