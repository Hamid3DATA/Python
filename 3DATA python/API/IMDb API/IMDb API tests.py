import json

import requests

url = "https://imdb8.p.rapidapi.com/title/get-ratings"
auto_complete_endpoint = "https://imdb8.p.rapidapi.com/auto-complete"

user_search = input("show you want to know about")
user_search_querystring = {"q": user_search}
ahaha = "tt0417299"
querystring = {"tconst": ahaha}


headers = {
    "X-RapidAPI-Key": "5791ff7ddemsh3d086b941302499p1ffa92jsn7c1f74363bc1",
    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}
response2 = requests.request("GET", auto_complete_endpoint, headers=headers, params=user_search_querystring)
user_search_id = json.dumps(response2.json()["d"][0]["id"])

response = requests.request("GET", url, headers=headers, params=querystring)
json_data = json.dumps(response.json()["rating"])

print(response)
print(user_search_id)
print(json_data)
