import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

language_from = input("What language do you want to translate from? (language 2 letter code)")

language_to = input("What language do you want to translate to? (language 2 letter code)")

text = input("What do you want to translate?")

payload = {
	"q": text,
	"target": language_to.lower(),
	"source": language_from.lower()
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "5791ff7ddemsh3d086b941302499p1ffa92jsn7c1f74363bc1",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

translation = response.json()["data"]["translations"][0]["translatedText"]
translation = translation.replace("'", "")

print(translation)
print("")

print("Warning! This translation may not be accurate, use at your own risk")
