import requests
import json

number = 0

help = 0
producers = []
licensors = []
studios = []
genres = []
explicit_genres = []

help2 = 0


name = input("Put in anime name")
print("")

url = "https://api.jikan.moe/v4/anime?q=" + name

r = requests.request("GET", url)

try:
  title = json.dumps(r.json()["data"][number]["title"])
except IndexError:
  print("it seems like there is no anime that goes by: " + name)
  quit()


question = input("is " + title +" the one you are looking for?")
print("")

while question != "yes":

  number += 1
  
  try:
    title = json.dumps(r.json()["data"][number]["title"])
  except IndexError:
    print("it seems like there is nothing left")
    quit()

  question = input("is " + title +" the one you are looking for?")
  print("")


title_english = json.dumps(r.json()["data"][number]["title_english"])
title_japanese = json.dumps(r.json()["data"][number]["title_japanese"])

trailer = json.dumps(r.json()["data"][number]["trailer"]["url"])

type = json.dumps(r.json()["data"][number]["type"])
source = json.dumps(r.json()["data"][number]["source"])
episodes = json.dumps(r.json()["data"][number]["episodes"])

status = json.dumps(r.json()["data"][number]["status"])

airing = json.dumps(r.json()["data"][number]["airing"])

aired_from = json.dumps(r.json()["data"][number]["aired"]["from"])
aired_to = json.dumps(r.json()["data"][number]["aired"]["to"])

aired_prop_from_day = json.dumps(r.json()["data"][number]["aired"]["prop"]["from"]["day"])
aired_prop_from_month = json.dumps(r.json()["data"][number]["aired"]["prop"]["from"]["month"])
aired_prop_from_year = json.dumps(r.json()["data"][number]["aired"]["prop"]["from"]["year"])

aired_prop_to_day = json.dumps(r.json()["data"][number]["aired"]["prop"]["to"]["day"])
aired_prop_to_month = json.dumps(r.json()["data"][number]["aired"]["prop"]["to"]["month"])
aired_prop_to_year = json.dumps(r.json()["data"][number]["aired"]["prop"]["to"]["year"])

string = json.dumps(r.json()["data"][number]["aired"]["string"])

duration = json.dumps(r.json()["data"][number]["duration"])

rating = json.dumps(r.json()["data"][number]["rating"])

score = json.dumps(r.json()["data"][number]["score"])
scored_by = json.dumps(r.json()["data"][number]["scored_by"])
rank = json.dumps(r.json()["data"][number]["rank"])
popularity = json.dumps(r.json()["data"][number]["popularity"])

synopsis = json.dumps(r.json()["data"][number]["synopsis"])

background = json.dumps(r.json()["data"][number]["background"])

season = json.dumps(r.json()["data"][number]["season"])
year = json.dumps(r.json()["data"][number]["year"])

broadcast_day = json.dumps(r.json()["data"][number]["broadcast"]["day"])
broadcast_time = json.dumps(r.json()["data"][number]["broadcast"]["time"])
broadcast_timezone = json.dumps(r.json()["data"][number]["broadcast"]["timezone"])
broadcast_string = json.dumps(r.json()["data"][number]["broadcast"]["string"])


try:
  producer = json.dumps(r.json()["data"][number]["producers"][0]["name"])
except IndexError:
  producers = "[]"
  help2 = 1

if help2 != 1:
  while True:
    try:
      producer = json.dumps(r.json()["data"][number]["producers"][help]["name"])
    except IndexError:
      break
    producer = producer.replace('"', '')
    producers.append(producer)
    help += 1
help = 0
help2 = 0


try:
  license = json.dumps(r.json()["data"][number]["licensors"][0]["name"])
except IndexError:
  licensors = "[]"
  help2 = 1

if help2 != 1:
  while True:
    try:
      license = json.dumps(r.json()["data"][number]["licensors"][help]["name"])
    except IndexError:
      break
    license = license.replace('"', '')
    licensors.append(license)
    help += 1
help = 0
help2 = 0


try: 
  studio = json.dumps(r.json()["data"][number]["studios"][0]["name"])
except IndexError:
  studios = "[]"


try:
  studio = json.dumps(r.json()["data"][number]["studios"][0]["name"])
except IndexError:
  studio = "[]"
  help2 = 1

if help2 != 1:
  while True:
    try:
      studio = json.dumps(r.json()["data"][number]["studios"][help]["name"])
    except IndexError:
      break
    studio = studio.replace('"', '')
    studios.append(studio)
    help += 1
help = 0
help2 = 0


try:
  genre = json.dumps(r.json()["data"][number]["genres"][0]["name"])
except IndexError:
  genres = "[]"
  help2 = 1

if help2 != 1:
  while True:
    try:
      genre = json.dumps(r.json()["data"][number]["genres"][help]["name"])
    except IndexError:
      break
    genre = genre.replace('"', '')
    genres.append(genre)
    help += 1
help = 0
help2 = 0


try:
  explicit_genre = json.dumps(r.json()["data"][number]["explicit_genres"][0]["name"])
except IndexError:
  explicit_genres = "[]"
  help2 = 1

if help2 != 1:
  while True:
    try:
      explicit_genre = json.dumps(r.json()["data"][number]["licensors"][help]["name"])
    except IndexError:
      break
    explicit_genre = explicit_genre.replace('"', '')
    explicit_genres.append(explicit_genre)
    help += 1
help = 0
help2 = 0


try: 
  demographics = json.dumps(r.json()["data"][number]["demographics"][0]["name"])
except IndexError:
  demographics = "[]"


print("")
print("title: " + title)

if title_english != "null":
  print("title english: " + title_english)

if title_japanese != "null":
  print("title japanese: " + title_japanese)
print("")


if trailer != "null":
  print("trailer: " + trailer)
  print("")

print("type: " + type)
print("source: " + source)

if episodes != "null":
  print("episodes: " + episodes)
print("")

print("status: " + status)
print("")

if aired_from != "null":
  print("aired from: " + aired_from)

if airing == "false" and episodes != "1" and episodes != "null":
  print("aired to: " + aired_to)
  print("")
else:
  help2 = 1

if help2 == 1:
  print ("")
  help2 = 0

if aired_prop_from_day != "null" or aired_prop_from_month != "null" or aired_prop_from_year != "null":
  print("aired from:")
  print("day: " + aired_prop_from_day)
  print("month: " + aired_prop_from_month)
  print("year: " + aired_prop_from_year)
  print("")

if airing == "false" and episodes != "1" and episodes != "null":
  print("aired to:")
  print("day: " + aired_prop_to_day)
  print("month: " + aired_prop_to_month)
  print("year: " + aired_prop_to_year)
  print("")
  print("string: " + string)
  print("")

if type == '"Movie"':
  print("string: " + string)
  print("")


if duration != '"Unknown"':
  print("duration: " + duration)
  print("")

if rating != "null":
  print("rating: " + rating)
  print("")

if score != "null":
  print("score: " + score)

if scored_by != "null":
  print("scored by: " + scored_by)

if rank != "null":
  print("rank: " + rank)
  
print("popularity: " + popularity)
print("")

if synopsis != "null":
  print("synopsis: " + synopsis)
  print("")

if background != "null":
  print("background: " + background)
  print("")

if season != "null":
  print("season: " + season)

if year != "null":
  print("year: " + year)
  print("")

if broadcast_day != "null" and broadcast_time != "null" and broadcast_timezone != "null" and broadcast_string != '"Unknown"' or broadcast_day != "null" and broadcast_time != "null" and broadcast_timezone != "null" and broadcast_string != "null":
  print("broadcast:")
  print("day: " + broadcast_day)
  print("time: " + broadcast_time)
  print("timezone: " + broadcast_timezone)
  print("string: " + broadcast_string)
  print("")

if producers != "[]":
  print("producers: " + str(producers))
  print("")

if licensors != "[]":
  print("licensors: " + str(licensors))
  print("")

if studios != "[]":
  print("studios: " + str(studios))
  print("")

if genres != "[]":
  print("genres: " + str(genres))
  print("")

if explicit_genres != "[]":
  print("explicit genres: " + str(explicit_genres))
  print("")

if demographics != "[]":
  print("demographics: " + demographics)
