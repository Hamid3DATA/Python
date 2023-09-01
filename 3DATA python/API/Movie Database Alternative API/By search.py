import requests

url = "https://movie-database-alternative.p.rapidapi.com/"

querystring = {"s": "Avengers Endgame", "r": "json", "page": "1"}

headers = {
    "X-RapidAPI-Key": "5791ff7ddemsh3d086b941302499p1ffa92jsn7c1f74363bc1",
    "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
