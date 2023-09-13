import requests
import json

#"https://api.agify.io/?name=" after '=' you can type the name"


name_selected = input("Put in a random name")

guess_age_endpoint = "https://api.agify.io/?name=" + name_selected.lower()
guess_age = requests.request("GET", guess_age_endpoint)

count = json.dumps(guess_age.json()["count"])
name = json.dumps(guess_age.json()["name"])
age = json.dumps(guess_age.json()["age"])

if count == ("0"):
  print("")
  print("The name you have written is not in our list, please try another name")
  exit()

print("count: " + count)
print("name: " + name)
print("")

user_guess = input("How old do you think this person is?")

if user_guess > age:
    age_difference = int(user_guess) - int(age)
elif age > user_guess:
    age_difference = int(age) - int(user_guess)

if user_guess == age:
    print("")
    print("CORRECT")
    print(name + " is indeed " + age + " years old!")
else:
    print("")
    print("INCORRECT")
    print("")
    print(name + " is actually " + age + " years old!")
    
    if user_guess > age:
      print("")
      print("you were off by " + str(age_difference) + " year(s)")
    elif age > user_guess:
      print("")
      print("you were off by " + str(age_difference) + " year(s)")
