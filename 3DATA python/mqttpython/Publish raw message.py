import paho.mqtt.client as mqttClient
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


Connected = False  # global variable for the state of the connection

broker_address = "192.168.1.197"
port = 1883
topic = "shellies/shellycolorbulb-3494546B6456/color/0/command"


client = mqttClient.Client("Python")  # create new instance
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

while not Connected:  # Wait for connection
    time.sleep(0.1)

try:
    while True:
        value = input('Enter the message:')
        client.publish(topic, value)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()
