import requests
import json

help = 0

cat_info_endpoint = "https://catfact.ninja/fact"


cat_fact = requests.request("GET", cat_info_endpoint)

fact = json.dumps(cat_fact.json()["fact"])


user_answer = input("Do you want to know a random cat fact? (yes/no)")

if user_answer.lower() == "yeah" or user_answer.lower() == "yea" or user_answer.lower() == "ye" or user_answer.lower() == "y" or user_answer.lower() == "yes":
    user_answer = "yes"
elif user_answer.lower() == "nah" or user_answer.lower() == "na" or user_answer.lower() == "n" or user_answer.lower() == "no":
    user_answer = "no"

if user_answer != "yes" and user_answer != "no":
    while help == 0:
        print("it was a simple yes or no question")
        print("")
        user_answer = input("Do you want to know a random cat fact? (yes/no)")

        if user_answer.lower() == "yeah" or user_answer.lower() == "yea" or user_answer.lower() == "ye" or user_answer.lower() == "y":
            user_answer = "yes"
        elif user_answer.lower() == "nah" or user_answer.lower() == "na" or user_answer.lower() == "n":
            user_answer = "no"

        if user_answer.lower() == "yes" or user_answer.lower() == "no":
            help += 1

if user_answer.lower() == "yes":
    print("did you know that: " + fact)
elif user_answer.lower() == "no":
    print("ok...☹")