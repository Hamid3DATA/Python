import requests  # for using API
import xml.etree.ElementTree as ET  # for parsing XML
import json

special_signs = ["{", "}", '"']

name = input("type inn an anime/manga name")
print("")
print("")
print("")


request_url = 'https://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=~' + name

r = requests.get(request_url)  # call API

root = ET.fromstring(r.content)  # parse XML

# loop through each "info" element in the XML 
for info in root.iter('info'):
  
  help = json.dumps(info.attrib)
  
  for x in help:
    for y in special_signs:
      if y is x:
        help = help.replace(x, "")
  
    
  print(help)
  print(info.text)
  print("")