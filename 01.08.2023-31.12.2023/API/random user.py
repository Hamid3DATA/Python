import requests
import json

endpoint = "https://randomuser.me/api/"

user_request = requests.request("GET", endpoint)

user = json.dumps(user_request.json()["results"][0]["name"]["first"])

user = user.replace('"', '')

print(user)