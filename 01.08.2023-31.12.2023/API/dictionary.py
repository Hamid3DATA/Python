import requests
import json

count = 0
count2 = 0
help = 0

word = input("type in your word: ")
print("")

url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word

r = requests.request("GET", url)

try:
  fornow = json.dumps(r.json()[count])
except KeyError:
  print("It seems like there is no word " '"'  + word + '"' + " in our dictionary")
  exit()

while True:
  try:
    fornow = json.dumps(r.json()[count])
    count += 1
  except IndexError:
    break

answer = input("We found " + str(count) + " meaning(s) of that word, which one would you like to see? (1 - " + str(count) + ")")
print("")
count -= 1
answer = int(answer) - 1

while True:
  try:
    fornow = json.dumps(r.json()[answer]["meanings"][count2])
    count2 += 1
  except IndexError:
    break
answer2 = input("We have found " + str(count2) + " definition(s) of that word, which one would you like to see?(1 - " + str(count2) + ")")
print("")
count2 -= 1
answer2 = int(answer2) - 1



word = json.dumps(r.json()[answer]["word"])

try:
  phonetic = json.dumps(r.json()[answer]["phonetic"])
except KeyError:
  phonetic = ""

try:
  text = json.dumps(r.json()[0]["phonetics"][answer]["text"])
except KeyError:
  text = ""
except IndexError:
  text = ""

try:
  audio = json.dumps(r.json()[0]["phonetics"][answer]["audio"])
except IndexError:
  audio = ""

try:
  sourceURL = json.dumps(r.json()[answer]["phonetics"][0]["sourceUrl"])
except KeyError:
  sourceURL = ""
except IndexError:
  sourceURL = ""


partofspeech = json.dumps(r.json()[answer]["meanings"][answer2]["partOfSpeech"])

print("word: " + word)
print("")

print("phonetic: " + phonetic)
print("")

print("text: " + text)
print("")

print("audio: " + audio)
print("")

print("sourceURL: " + sourceURL)
print("")
print("")
print("")

print("partOfSpeech: " + partofspeech)
print("")


while True:
  try:
    definition = json.dumps(r.json()[answer]["meanings"][answer2]["definitions"][help]["definition"])
    print("definition: " + definition)
    print("")
  except IndexError:
    break

  try:
    example = json.dumps(r.json()[answer]["meanings"][answer2]["definitions"][help]["example"])
    print("example: " + example)
    print("")
  except KeyError:
    example = ""

  synonyms = json.dumps(r.json()[answer]["meanings"][answer2]["definitions"][help]["synonyms"])
  if synonyms != "[]":
    print("synonyms: " + synonyms)
    print("")

  antonyms = json.dumps(r.json()[answer]["meanings"][answer2]["definitions"][help]["antonyms"])
  if antonyms != "[]":
    print("antonyms: " + antonyms)
    print("")

  help += 1
