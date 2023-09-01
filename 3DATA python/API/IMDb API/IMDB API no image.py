import requests
import json
import webbrowser
import time

auto_complete_endpoint = "https://imdb8.p.rapidapi.com/auto-complete"
get_ratings_endpoint = "https://imdb8.p.rapidapi.com/title/get-ratings"
get_base_endpoint = "https://imdb8.p.rapidapi.com/title/get-base"
get_plot_endpoint = "https://imdb8.p.rapidapi.com/title/get-plots"

user_search = input("What show do you want to know about?")

user_search_querystring = {"q": user_search}

headers = {
    "X-RapidAPI-Key": "5791ff7ddemsh3d086b941302499p1ffa92jsn7c1f74363bc1",
    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

search_response = requests.request("GET", auto_complete_endpoint, headers=headers, params=user_search_querystring)
user_search_id = json.dumps(search_response.json()["d"][0]["id"])
user_search_genre = json.dumps(search_response.json()["d"][0]["q"])
user_search_years = json.dumps(search_response.json()["d"][0]["y"])

the_id = user_search_id.replace('"', '')
id_querystring = {"tconst": the_id}

id_response = requests.request("GET", get_ratings_endpoint, headers=headers, params=id_querystring)
user_search_rating = json.dumps(id_response.json()["rating"])

image_response = requests.request("GET", get_base_endpoint, headers=headers, params=id_querystring)
image_url = json.dumps(image_response.json()["image"]["url"])

plot_response = requests.request("GET", get_plot_endpoint, headers=headers, params=id_querystring)
plot_text = json.dumps(plot_response.json()["plots"][0]["text"])

print(f"ID: {user_search_id}")
print(f"Genre: {user_search_genre}")
print(f"Year: {user_search_years}")
print(f"Rating: {user_search_rating}")
time.sleep(5)
seconds = 5
while True:
    print("Image in:")
    print(f"00:0{seconds}")
    seconds -= 1
    time.sleep(1)
    if seconds == 0:
        break
webbrowser.open(image_url)

plot = input("do you want to know the plot?(yes/no)")
if plot == "yes":
    print(plot_text)
else:
    print("nvm")
