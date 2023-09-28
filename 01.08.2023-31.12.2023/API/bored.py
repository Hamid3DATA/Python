import requests
import json

# look more into the documentation: https://www.boredapi.com/documentation

help = 0


print("[1] to search by activity key/id")
print("[2] to search by type")
print("[3] to search by the amount of participants")
print("[4] to search by price")
print("[5] to search by price range")
print("[6] to search by accessibility")
print("[7] to search by accessibility range")
print("[8] to get a random activity")
user_answer = input("Select one of the above: ")


if user_answer == "1":

    print("")
    key = input("type in the activity id: ")

    key_activity_endpoint = "https://www.boredapi.com/api/activity?key=" + key
    key_activity = requests.request("GET", key_activity_endpoint)

    try:
        activity = json.dumps(key_activity.json()["activity"])
    except KeyError:
        print("")
        print("there is no activity with the key value that you have put")
        help = 1
    
    if help != 1:

        type = json.dumps(key_activity.json()["type"])
        participants = json.dumps(key_activity.json()["participants"])
        price = json.dumps(key_activity.json()["price"])
        accessibility = json.dumps(key_activity.json()["accessibility"])

        print("")
        print("you can: " + activity)
        print("type: " + type)
        print("amount of people needed: " + participants)
        print("price: " + price)
        print("accessibility: " + accessibility)

if user_answer == "2":

    print("")
    print("(education, recreational, social, diy, charity, cooking, relaxation, music, busywork)")
    the_type = input("type in activity type: ")

    type_activity_endpoint = "https://www.boredapi.com/api/activity?type=" + the_type.lower()
    type_activity = requests.request("GET", type_activity_endpoint)

    try:
        activity = json.dumps(type_activity.json()["activity"])
    except KeyError:
        print("")
        print("doublecheck your spelling")
        help = 1
    
    if help != 1:
        type = json.dumps(type_activity.json()["type"])
        participants = json.dumps(type_activity.json()["participants"])
        price = json.dumps(type_activity.json()["price"])
        accessibility = json.dumps(type_activity.json()["accessibility"])
        
        print("")
        print("you can: " + activity)
        print("type: " + type)
        print("amount of people needed: " + participants)
        print("price: " + price)
        print("accessibility: " + accessibility)

elif user_answer == "3":

    print("")
    amount = input("type in amount of participants in the activity (1 - 5): ")

    participants_activity_endpoint = "https://www.boredapi.com/api/activity?participants=" + amount
    participants_activity = requests.request("GET", participants_activity_endpoint)


    if amount == "1" or amount == "2" or amount == "3" or amount == "4" or amount == "5":

        activity = json.dumps(participants_activity.json()["activity"])
        type = json.dumps(participants_activity.json()["type"])
        participants = json.dumps(participants_activity.json()["participants"])
        price = json.dumps(participants_activity.json()["price"])
        accessibility = json.dumps(participants_activity.json()["accessibility"])

        print("")
        print("you can: " + activity)
        print("type: " + type)
        print("amount of people needed: " + participants)
        print("price: " + price)
        print("accessibility: " + accessibility)

    else:
        print("you can only type 1 - 5 nothing else")

elif user_answer == "4":

    print("")
    print("0.0 - 1.0 (cost of the event with 0.0 being free)")
    the_price = input("type in the price: ")

    try:
        float(the_price)
    except ValueError:
        print("")
        print("you should type a float number between 0.0 - 1.0")
        help = 1
    
    if help != 1:
        if float(the_price) == 0.0  or float(the_price) == 1.0 or float(the_price) > 0.0 and float(the_price) < 1.0:

            price_activity_endpoint = "https://www.boredapi.com/api/activity?price=" + the_price
            price_activity = requests.request("GET", price_activity_endpoint)

            try:
                activity = json.dumps(price_activity.json()["activity"])
            except KeyError:
                print("")
                print("There is no activity for the price you have selected - " + the_price)
                help = 1

            if help == 0:
                type = json.dumps(price_activity.json()["type"])
                participants = json.dumps(price_activity.json()["participants"])
                price = json.dumps(price_activity.json()["price"])
                accessibility = json.dumps(price_activity.json()["accessibility"])

                print("")
                print("you can: " + activity)
                print("type: " + type)
                print("amount of people needed: " + participants)
                print("price: " + price)
                print("accessibility: " + accessibility)

        else:
            print("you can only type float numbers between 0.0 and 1.0")
        
elif user_answer == "5":

    print("")
    print("type in the price range from 0.0 - 1.0 with 0.0 being free")
    min_range = input("minimum price: ")
    max_range = input("maximum price: ")

    try:
        float(min_range)
        float(max_range)
    except ValueError:
        print("")
        print("you should type a float number between 0.0 - 1.0")
        help = 1

    if help != 1:
        if float(min_range) == 0.0 or float(min_range) == 1.0 or float(min_range) > 0.0 and float(min_range) < 1.0 and float(max_range) == 0.0 or float(max_range) == 1.0 or float(max_range) > 0.0 and float(max_range) < 1.0:

            price_range_activity_endpoint = "https://www.boredapi.com/api/activity?minprice=" + min_range + "&maxprice=" + max_range
            price_range_activity = requests.request("GET", price_range_activity_endpoint)

            try:
                activity = json.dumps(price_range_activity.json()["activity"])
            except KeyError:
                print("")
                print("There is no activity for the price you have selected: "  + min_range + " - " + max_range)
                help = 1

            if help == 0:
                type = json.dumps(price_range_activity.json()["type"])
                participants = json.dumps(price_range_activity.json()["participants"])
                price = json.dumps(price_range_activity.json()["price"])
                accessibility = json.dumps(price_range_activity.json()["accessibility"])

                print("")
                print("you can: " + activity)
                print("type: " + type)
                print("amount of people needed: " + participants)
                print("price: " + price)
                print("accessibility: " + accessibility)

        else:
            print("you can only type float numbers between 0.0 and 1.0")

elif user_answer == "6":
    
    print("")
    print("the range is from 0.0 - 1.0 with zero being most accessible")
    the_accessibility = input("type in accessibility value: ")

    try:
        float(the_accessibility)
    except ValueError:
        print("")
        print("you should type a float number between 0.0 - 1.0")
        help = 1

    if help != 1:
        if float(the_accessibility) == 0.0 or float(the_accessibility) == 1.0 or float(the_accessibility) > 0.0 and float(the_accessibility) < 1.0:

            accessibility_activity_endpoint = "https://www.boredapi.com/api/activity?accessibility=" + the_accessibility
            accessibility_activity = requests.request("GET", accessibility_activity_endpoint)

            try:
                activity = json.dumps(accessibility_activity.json()["activity"])
            except KeyError:
                print("")
                print("There is no activity for the accessibility that you have selected - " + the_accessibility)
                help = 1

            if help == 0:
                type = json.dumps(accessibility_activity.json()["type"])
                participants = json.dumps(accessibility_activity.json()["participants"])
                price = json.dumps(accessibility_activity.json()["price"])
                accessibility = json.dumps(accessibility_activity.json()["accessibility"])

                print("")
                print("you can: " + activity)
                print("type: " + type)
                print("amount of people needed: " + participants)
                print("price: " + price)
                print("accessibility: " + accessibility)

        else:
            print("you can only type float numbers between 0.0 and 1.0")

elif user_answer == "7":
    
    print("")
    print("type in the price range from 0.0 - 1.0 with 0.0 being free")
    min_range = input("minimum accessability value: ")
    max_range = input("maximum accessability value: ")

    try:
        float(min_range)
        float(max_range)
    except ValueError:
        print("")
        print("you should type a float number between 0.0 - 1.0")
        help = 1

    if help != 1:
        if float(min_range) == 0.0 or float(min_range) == 1.0 or float(min_range) > 0.0 and float(min_range) < 1.0 and float(max_range) == 0.0 or float(max_range) == 1.0 or float(max_range) > 0.0 and float(max_range) < 1.0:

            accessibility_range_activity_endpoint = "https://www.boredapi.com/api/activity?minaccessibility=" + min_range + "&maxaccessibility=" + max_range
            accessibility_range_activity = requests.request("GET", accessibility_range_activity_endpoint)

            try:
                activity = json.dumps(accessibility_range_activity.json()["activity"])
            except KeyError:
                print("")
                print("There is no activity for the price you have selected: "  + min_range + " - " + max_range)
                help = 1

            if help == 0:
                type = json.dumps(accessibility_range_activity.json()["type"])
                participants = json.dumps(accessibility_range_activity.json()["participants"])
                price = json.dumps(accessibility_range_activity.json()["price"])
                accessibility = json.dumps(accessibility_range_activity.json()["accessibility"])

                print("")
                print("you can: " + activity)
                print("type: " + type)
                print("amount of people needed: " + participants)
                print("price: " + price)
                print("accessibility: " + accessibility)

        else:
            print("you can only type float numbers between 0.0 and 1.0")

elif user_answer == "8":
    random_activity_endpoint = "https://www.boredapi.com/api/activity/"
    random_activity = requests.request("GET", random_activity_endpoint)
    
    activity = json.dumps(random_activity.json()["activity"])
    type = json.dumps(random_activity.json()["type"])
    participants = json.dumps(random_activity.json()["participants"])
    price = json.dumps(random_activity.json()["price"])
    accessibility = json.dumps(random_activity.json()["accessibility"])

    print("")
    print("you can: " + activity)
    print("type: " + type)
    print("amount of people needed: " + participants)
    print("price: " + price)
    print("accessibility: " + accessibility)

else:
    print("")
    print("That was not on the list :/")
