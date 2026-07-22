print("Line 1")

import requests
print("Line 2")

url = "https://jsonplaceholder.typicode.com/users"
print("Line 3")

try:
    print("Before request")
    response = requests.get(url, timeout=10)
    print("After request")
    print("Status Code:", response.status_code)
except Exception as e:
    print("Exception:", e)

print("Program Finished")
