import requests
import webbrowser

r = requests.request("GET", "https://yesno.wtf/api")

url = r.json()["image"]
answer = r.json()["answer"]

webbrowser.open(url)
print("")
print(answer)
print("")
print(url)
