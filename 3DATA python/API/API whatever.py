import requests
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
response.headers.get("Content-Type")

response.json()

print(response.json())
