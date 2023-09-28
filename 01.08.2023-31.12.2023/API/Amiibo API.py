import requests
import json

help = 0
help2 = 0
answer = ""

print("[1] Search by character")
print("[2] Search by name")

try:
  choice = int(input (""))
except ValueError:
  print("type either 1 or 2")
  exit()



if choice == 1:
  
  character = input("type in the character: ")
  r = requests.request("GET", "https://www.amiiboapi.com/api/amiibo/?character=" + character)
  
  while answer != "yes":
    try:
      amiiboSeries = r.json()["amiibo"][help]["amiiboSeries"]
    except IndexError:
      print("Seems like there are no more Amiibos with that character on our list")
      exit()
    
    amiiboCharacter = r.json()["amiibo"][help]["character"]
    amiiboGameSeries = r.json()["amiibo"][help]["gameSeries"]
    amiiboHead = r.json()["amiibo"][help]["head"]
    amiiboImage = r.json()["amiibo"][help]["image"]
    amiiboName = r.json()["amiibo"][help]["name"]
    amiiboRelease = r.json()["amiibo"][help]["release"]
    amiiboTail = r.json()["amiibo"][help]["tail"]
    amiiboType = r.json()["amiibo"][help]["type"]
    
    print("")
    print(amiiboSeries)
    print(amiiboCharacter)
    print(amiiboGameSeries)
    print(amiiboHead)
    print(amiiboImage)
    print(amiiboName)
    print(amiiboRelease)
    print(amiiboTail)
    print(amiiboType)
    
    print("")
    answer = input("Is this the one you are looking for? ")
    
    if answer == "yes":
      print("")
      answer = input("Whould you like to see the use of this amiibo? ")
      
      if answer == "yes":
        
        r = requests.request("GET", "https://www.amiiboapi.com/api/amiibo/?character=" + character + "&showusage")
        print("")
        console = input("What console whould you like to see usage on? (3DS, Switch, WiiU)")
        
        if console.lower() == "3ds":
          
          while True:
            
            try:
              game = r.json()["amiibo"][help]["games3DS"][help2]["gameName"]
            except IndexError:
              break
              
            usage = r.json()["amiibo"][help]["games3DS"][help2]["amiiboUsage"]
            
            print("")
            print(game)
            print(usage)
            print("")
            
            help2 += 1
          
        elif console.lower() == "switch":
          
          while True:
            
            try:
              game = r.json()["amiibo"][help]["gamesSwitch"][help2]["gameName"]
            except IndexError:
              break
              
            usage = r.json()["amiibo"][help]["gamesSwitch"][help2]["amiiboUsage"]
            
            print("")
            print(game)
            print(usage)
            print("")
            
            help2 += 1
          
        elif console.lower() == "wiiu":
          
          while True:
            
            try:
              game = r.json()["amiibo"][help]["gamesWiiU"][help2]["gameName"]
            except IndexError:
              break
              
            usage = r.json()["amiibo"][help]["gamesWiiU"][help2]["amiiboUsage"]
            
            print("")
            print(game)
            print(usage)
            print("")
            
            help2 += 1
          
        exit()
      
      else:
        exit()

    help += 1



elif choice == 2:
  
  name = input("Type in the name: ")
  
  r = requests.request("GET", "https://www.amiiboapi.com/api/amiibo/?name=" + name)
    
  while answer != "yes":
    try:
      amiiboSeries = r.json()["amiibo"][help]["amiiboSeries"]
    except IndexError:
      print("Seems like there are no more Amiibos with than name on our list")
      exit()
  
    amiiboCharacter = r.json()["amiibo"][help]["character"]
    amiiboGameSeries = r.json()["amiibo"][help]["gameSeries"]
    amiiboHead = r.json()["amiibo"][help]["head"]
    amiiboImage = r.json()["amiibo"][help]["image"]
    amiiboName = r.json()["amiibo"][help]["name"]
    amiiboRelease = r.json()["amiibo"][help]["release"]
    amiiboTail = r.json()["amiibo"][help]["tail"]
    amiiboType = r.json()["amiibo"][help]["type"]
    
    print("")
    print(amiiboSeries)
    print(amiiboCharacter)
    print(amiiboGameSeries)
    print(amiiboHead)
    print(amiiboImage)
    print(amiiboName)
    print(amiiboRelease)
    print(amiiboTail)
    print(amiiboType)
    
    print("")
    answer = input("Is this the one you are looking for? ")
    
    
    if answer == "yes":
      print("")
      answer = input("Whould you like to see the use of this amiibo? ")
      
      if answer == "yes":
        
        r = requests.request("GET", "https://www.amiiboapi.com/api/amiibo/?name=" + name + "&showusage")
        print("")
        console = input("What console whould you like to see usage on? (3DS, Switch, WiiU)")
        
        if console.lower() == "3ds":
          
          while True:
            
            try:
              game = r.json()["amiibo"][help]["games3DS"][help2]["gameName"]
            except IndexError:
              break
              
            usage = r.json()["amiibo"][help]["games3DS"][help2]["amiiboUsage"]
            
            print("")
            print(game)
            print(usage)
            print("")
            
            help2 += 1
          
        elif console.lower() == "switch":
          
          while True:
            
            try:
              game = r.json()["amiibo"][help]["gamesSwitch"][help2]["gameName"]
            except IndexError:
              break
              
            usage = r.json()["amiibo"][help]["gamesSwitch"][help2]["amiiboUsage"]
            
            print("")
            print(game)
            print(usage)
            print("")
            
            help2 += 1
          
        elif console.lower() == "wiiu":
          
          while True:
            
            try:
              game = r.json()["amiibo"][help]["gamesWiiU"][help2]["gameName"]
            except IndexError:
              break
              
            usage = r.json()["amiibo"][help]["gamesWiiU"][help2]["amiiboUsage"]
            
            print("")
            print(game)
            print(usage)
            print("")
            
            help2 += 1
          
        exit()
      
      else:
        exit()

    help += 1
