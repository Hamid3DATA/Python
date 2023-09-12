import requests
import json

#"https://api.agify.io/?name=" after '=' you can type the name"


name_endpoint = "https://randomuser.me/api/"
user_request = requests.request("GET", name_endpoint)

user_name = json.dumps(user_request.json()["results"][0]["name"]["first"])
user_name = user_name.replace('"', '')


guess_age_endpoint = "https://api.agify.io/?name=" + user_name.lower()
guess_age = requests.request("GET", guess_age_endpoint)

count = json.dumps(guess_age.json()["count"])
name = json.dumps(guess_age.json()["name"])
age = json.dumps(guess_age.json()["age"])


print("count: " + count)
print("name: " + name)
print("")


user_guess = input("How old do you think this person is?")

if user_guess == age:
    print("CORRECT")
    print(name + " is indeed " + age + " years old!")
else:
    print("")
    print("INCORRECT")
    
    print(name + " is actually " + age + " years old!")