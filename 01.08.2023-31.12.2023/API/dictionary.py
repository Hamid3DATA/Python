import requests
import json

help = 0
help2 = 0

word = input("type in your word: ")

url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word

r = requests.request("GET", url)

word = json.dumps(r.json()[0]["word"])
print("word: " + word)
print("")

phonetic = json.dumps(r.json()[0]["phonetic"])
print("phonetic: " + phonetic)
print("")

text = json.dumps(r.json()[0]["phonetics"][0]["text"])
print("text: " + text)
print("")

audio = json.dumps(r.json()[0]["phonetics"][0]["audio"])
print("audio: " + audio)
print("")

try:
  sourceURL = json.dumps(r.json()[0]["phonetics"][0]["sourceUrl"])
  print("sourceURL: " + sourceURL)
  print("")
except KeyError:
  sourceURL = ""

partofspeech = json.dumps(r.json()[0]["meanings"][help]["partOfSpeech"])
print("partOfSpeech: " + partofspeech)
print("")

definition = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["definition"])
print("definition: " + definition)
print("")

example = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["example"])
print("example: " + example)
print("")

synonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["synonyms"])
print("synonyms: " + synonyms)
print("")

antonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["antonyms"])
print("antonyms: " + antonyms)
print("")


while True:
  help2 += 1
  try:
    definition = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["definition"])
    print("definition: " + definition)
    print("")

    example = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["example"])
    print("example: " + example)
    print("")

    synonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["synonyms"])
    print("synonyms: " + synonyms)
    print("")

    antonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["antonyms"])
    print("antonyms: " + antonyms)
    print("")
  except IndexError:
    break
  except KeyError:
    break

help2 = 0

while True:
  help += 1
  try:
    partofspeech = json.dumps(r.json()[0]["meanings"][help]["partOfSpeech"])
    print("partOfSpeech: " + partofspeech)
    print("")

    definition = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["definition"])
    print("definition: " + definition)
    print("")

    example = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["example"])
    print("example: " + example)
    print("")

    synonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["synonyms"])
    print("synonyms: " + synonyms)
    print("")

    antonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["antonyms"])
    print("antonyms: " + antonyms)
    print("")
  except IndexError:
    break
  except KeyError:
    break
  
  help2 += 1
  try:
    definition = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["definition"])
    print("definition: " + definition)
    print("")

    example = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["example"])
    print("example: " + example)
    print("")

    synonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["synonyms"])
    print("synonyms: " + synonyms)
    print("")

    antonyms = json.dumps(r.json()[0]["meanings"][help]["definitions"][help2]["antonyms"])
    print("antonyms: " + antonyms)
    print("")
  except IndexError:
    break
  except KeyError:
    break