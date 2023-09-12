import requests
import json

#"https://api.agify.io/?name=" after '=' you can type the name"


name_selected = input("Put in a random name")

guess_age_endpoint = "https://api.agify.io/?name=" + name_selected.lower()
guess_age = requests.request("GET", guess_age_endpoint)

count = json.dumps(guess_age.json()["count"])
name = json.dumps(guess_age.json()["name"])
age = json.dumps(guess_age.json()["age"])


print("count: " + count)
print("name: " + name)
print("")

if count == ("0"):
  print("The name you have written is not in our list, please try another name")
  exit()

user_guess = input("How old do you think this person is?")

if user_guess == age:
    print("")
    print("CORRECT")
    print(name + " is indeed " + age + " years old!")
else:
    print("")
    print("INCORRECT")
    print(name + " is actually " + age + " years old!")
