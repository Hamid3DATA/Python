import requests
import json

# look more into the documentation: https://github.com/15Dkatz/official_joke_api


random_joke_endpoint = "https://official-joke-api.appspot.com/random_joke"

random_joke = requests.request("GET", random_joke_endpoint)




print("[1] for a random joke")
print("[2] for a random joke by genre")
print("[3] for a joke from ID")
user_answer = input("Pick one from the above")

if user_answer == "1":

    the_type = json.dumps(random_joke.json()["type"])
    the_setup = json.dumps(random_joke.json()["setup"])
    the_punchline = json.dumps(random_joke.json()["punchline"])

    print("type: " + the_type)
    print("setup: " + the_setup)
    print("punchline: " + the_punchline)

elif user_answer == "2":
    while True:

        print("")
        user_answer = input("What genre? - General, Programming")

        if user_answer.lower() == "general":

            general_joke_endpoint = "https://official-joke-api.appspot.com/jokes/general/random"
            
            general_joke = requests.request("GET", general_joke_endpoint)

            the_type = json.dumps(general_joke.json()["type"])
            the_setup = json.dumps(general_joke.json()["setup"])
            the_punchline = json.dumps(general_joke.json()["punchline"])

            print("type: " + the_type)
            print("setup: " + the_setup)
            print("punchline: " + the_punchline)

            break
        elif user_answer.lower() == "programming":

            programming_joke_endpoint = "https://official-joke-api.appspot.com/jokes/programming/random"
            
            programming_joke = requests.request("GET", programming_joke_endpoint)

            the_type = json.dumps(programming_joke.json()["type"])
            the_setup = json.dumps(programming_joke.json()["setup"])
            the_punchline = json.dumps(programming_joke.json()["punchline"])

            print("type: " + the_type)
            print("setup: " + the_setup)
            print("punchline: " + the_punchline)
            break
        else:
            print("Check your spelling")
elif user_answer == "3":
    id = input("type inn id from 1 - 409")

    id_joke_endpoint = "https://official-joke-api.appspot.com/jokes/" + id

    id_joke = requests.request("GET", id_joke_endpoint)

    id_type = json.dumps(id_joke.json()["type"])
    
    id_setup = json.dumps(id_joke.json()["setup"])
    
    id_punchline = json.dumps(id_joke.json()["punchline"])

    print("type: " + id_type)
    print("setup: " + id_setup)
    print("punchline: " + id_punchline)
else:
    print("please type 1, 2 or 3 nothing else")

