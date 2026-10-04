import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

data = response.json()

print("Status Code:", response.status_code)
# print("Headers:", response.headers)
# print("Title:", response.json()["title"])

print("Response:", data)
print("Title:", data["title"])