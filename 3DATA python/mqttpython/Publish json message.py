import paho.mqtt.client as mqttClient
import json


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


def on_publish(client, userdata, mid):
    print("Message Published...")


Connected = False  # global variable for the state of the connection

broker_address = "192.168.1.197"
port = 1883
topic = "shellies/shellycolorbulb-3494546B6456/color/0/set"

JSON_Object = json.dumps({
    "mode": "color",
    "red": 150,
    "green": 150,
    "blue": 150,
    "gain": 5,
    "brightness": 5,
    "white": 0,
    "temp": 4750,
    "effect": 2,
    "turn": "on"
})

client = mqttClient.Client("Python")  # create new instance
client.on_publish = on_publish  # print(Message Published...) - to indicate that the message has been sent
client.connect(broker_address, port=port)  # connect to broker
client.on_connect = on_connect  # attach function to callback

client.publish(topic, JSON_Object)  # topic - publish where    JSO_Object - the thing we want to publish
