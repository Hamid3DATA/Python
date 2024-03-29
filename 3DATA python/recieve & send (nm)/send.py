import socket
import json
UDP_IP = "192.168.1.103"
UDP_PORT = 5006

data = "Hello!"
MESSAGE = str.encode(data)
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
