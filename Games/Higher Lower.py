import random

tries = 0

pc = (random.randrange(1, 10))

while True:
  
  print("Guess the number i have chosen! (from 1 to 10)")
  guess = int(input())
  
  tries += 1
  
  if guess == pc:
      print("Correct, you have won!")
      quit()
  
  if tries == 3:
      print("Sorry, you have used more than 3 tries, my number was", pc)
      quit()
  
  if guess > pc:
    print("my number is lower")
  elif guess < pc:
    print("my number is higher")
