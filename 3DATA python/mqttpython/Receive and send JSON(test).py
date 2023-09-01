import paho.mqtt.client as mqttClient
import json

broker_address = "192.168.1.144"
port = 1883

topic = "shellies/shellycolorbulb-3494546B6456/color/0/set"

JSON_Object = json.dumps({
    "mode": "color",
    "red": 100,
    "green": 100,
    "blue": 0,
    "gain": 10,
    "brightness": 100,
    "white": 0,
    "temp": 4750,
    "effect": 0,
    "turn": "on"
})


def on_publish(client, userdata, mid):
    print("Message Published...")


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)
    client.publish(topic, JSON_Object)


def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload)  # <- do you mean this payload = {...} ?
    payload = json.loads(msg.payload)  # you can use json.loads to convert string to json
    print(payload['sepalWidth'])  # then you can check the value
    client.disconnect()  # Got message then disconnect


client = mqttClient.Client()

client.on_publish = on_publish

client.connect(broker_address, port)

client.publish(topic, JSON_Object)

client.disconnect()
