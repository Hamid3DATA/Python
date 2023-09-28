import requests
import json
import webbrowser

r = requests.request("GET", "https://yesno.wtf/api")

url = r.json()["image"]

webbrowser.open(url)
print(url)
