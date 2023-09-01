import json

JSON_Object = {
    "mode": "color",
    "red": 0,
    "green": 0,
    "blue": 255,
    "gain": 10,
    "brightness": 100,
    "white": 0,
    "temp": 4750,
    "effect": 0,
    "turn": "on"
}

JSON_Object_to_Python = json.dumps(JSON_Object)
print(JSON_Object)

