import requests

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Key": "5791ff7ddemsh3d086b941302499p1ffa92jsn7c1f74363bc1",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

setup = response.json()["body"][0]["setup"]
punchline = response.json()["body"][0]["punchline"]

print(setup)
print("")
print(punchline)
