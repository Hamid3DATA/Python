import requests
import json
import webbrowser
import time



help = 0

random_dog_image_endpoint = "https://dog.ceo/api/breeds/image/random"


random_dog_image = requests.request("GET", random_dog_image_endpoint)

url = json.dumps(random_dog_image.json()["message"])

url = url.replace('"', '')
print(url)


user_answer = input("Do you want to see a random dog image? (yes/no)")

if user_answer.lower() == "yeah" or user_answer.lower() == "yea" or user_answer.lower() == "ye" or user_answer.lower() == "y" or user_answer.lower() == "yes":
    user_answer = "yes"
elif user_answer.lower() == "nah" or user_answer.lower() == "na" or user_answer.lower() == "n" or user_answer.lower() == "no":
    user_answer = "no"

if user_answer != "yes" and user_answer != "no":
    while help == 0:
        print("it was a simple yes or no question")
        print("")
        user_answer = input("Do you want to see a random dog image? (yes/no)")
        print("")

        if user_answer.lower() == "yeah" or user_answer.lower() == "yea" or user_answer.lower() == "ye" or user_answer.lower() == "y":
            user_answer = "yes"
        elif user_answer.lower() == "nah" or user_answer.lower() == "na" or user_answer.lower() == "n":
            user_answer = "no"

        if user_answer.lower() == "yes" or user_answer.lower() == "no":
            help += 1

if user_answer.lower() == "yes":
    print("Good!")
    time.sleep(1)
    print("opening:")
    webbrowser.open(url)
elif user_answer.lower() == "no":
    print("ok...☹")