import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print("Status Code:", response.status_code)
# print("Response:", data)

for user in data:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("Company:", user["company"]["name"])
    print("-" * 40)

# Using lambda function to format user information
format_user = lambda u: f"{u['name']} | {u['email']} | {u['company']['name']}"
for user in data:
    print(format_user(user))