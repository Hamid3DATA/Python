import requests
import json
import webbrowser

print("print the data you want to be in the QR code")
data = input()

print("select the size of the QR Code in pixels (It's gonna be a square, so you select one side size onlyexample: 400)")
try:
  size = int(input())
except ValueError:
  print("it has to be a number!")
  exit()

url = "https://api.qrserver.com/v1/create-qr-code/?data=" + data + "&size=" + str(size) + "x" + str(size)

webbrowser.open(url)
print("")
print("if a page with the QR code didn't open by itself, go to this link:")
print(url)
