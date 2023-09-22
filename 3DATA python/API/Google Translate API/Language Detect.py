import requests
import json

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

text = input("Type inn anything in any language")
payload = "q= " + text
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "5791ff7ddemsh3d086b941302499p1ffa92jsn7c1f74363bc1",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

basic_response = json.dumps(response.json())

language = json.dumps(response.json()["data"]["detections"][0][0]["language"])
language = language.replace('"', '')

confidence = json.dumps(response.json()["data"]["detections"][0][0]["confidence"])


print("language: " + language)
print("confidence: " + confidence)
print("")
print("")
print("")
print(basic_response)
