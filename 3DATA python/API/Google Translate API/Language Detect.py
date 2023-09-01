import requests
import json

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = "q= hello, i can speak"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "5791ff7ddemsh3d086b941302499p1ffa92jsn7c1f74363bc1",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)
language = json.dumps(response.json())
print(language)
