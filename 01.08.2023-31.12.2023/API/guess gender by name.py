import requests
import json

#"https://api.genderize.io/?name=" after '=' you can type the name

help = 0

name_selected = input("Put in a random name")

guess_gender_endpoint = "https://api.genderize.io/?name=" + name_selected.lower()


guess_gender = requests.request("GET", guess_gender_endpoint)

count = json.dumps(guess_gender.json()["count"])
name = json.dumps(guess_gender.json()["name"])

gender = json.dumps(guess_gender.json()["gender"])
gender = gender.replace('"', '')

probability = json.dumps(guess_gender.json()["probability"])
probability = float(probability) * 100


print("count: " + count)
print("name: " + name)
print("")


user_guess = input("What gender do you think this person is? (male/female - boy/girl)")
print("")

if user_guess.lower() == "boy" or user_guess.lower() == "bo" or user_guess.lower() == "b" or user_guess.lower() == "mal" or user_guess.lower() == "ma" or user_guess.lower() == "m":
    user_guess = "male"
elif user_guess.lower() == "girl" or user_guess.lower() == "gir" or user_guess.lower() == "gi" or user_guess.lower() == "g" or user_guess.lower() == "femal" or user_guess.lower() == "fema" or user_guess.lower() == "fem" or user_guess.lower() == "fe" or user_guess.lower() == "f":
    user_guess = "female"


if user_guess != "male" and user_guess != "female":
    while help == 0:
        print("doublecheck you spelling")
        print("")
        user_guess = input("What gender do you think this person is? (male/female - boy/girl)")
        print("")

        if user_guess.lower() == "boy" or user_guess.lower() == "bo" or user_guess.lower() == "b" or user_guess.lower() == "mal" or user_guess.lower() == "ma" or user_guess.lower() == "m":
            user_guess = "male"
        elif user_guess.lower() == "girl" or user_guess.lower() == "gir" or user_guess.lower() == "gi" or user_guess.lower() == "g" or user_guess.lower() == "femal" or user_guess.lower() == "fema" or user_guess.lower() == "fem" or user_guess.lower() == "fe" or user_guess.lower() == "f":
            user_guess = "female"
        
        if user_guess.lower() == "male" or user_guess.lower() == "female":
            help += 1


if user_guess.lower() == gender:
    print("CORRECT")
    print("This person is: " + gender)
    print("With the probability of: " + str(probability) + "%")
    print("")
    print("")
    print("")
else:
    print("INCORECT")
    print(name + "is a " + gender)
    print("With the probability of: " + str(probability) + "%")
    print("")
    print("")
    print("")

print(guess_gender.json())