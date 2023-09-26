import random

tries = 1

pc = (random.randrange(1, 100))

print("Guess the number i have chosen! (from 1 to 100)")
guess = int(input())

previous_guess_difference = abs(guess - pc)

if previous_guess_difference > 20:
  print("Cold!")
  print("")

elif previous_guess_difference < 20:
  print("Warm!")
  print("")

elif previous_guess_difference < 10:
  print("Hot!")
  print("")

elif guess == pc:
  print("You Won! first try!")
  exit()

while True:
  print("Guess the number i have chosen! (from 1 to 100)")
  guess = int(input())
  
  guess_difference = abs(guess - pc)
  
  tries += 1
  
  if guess == pc:
    print("You Won! on your " + str(tries) + "th try!")
    exit()
  
  if guess_difference > previous_guess_difference:
    print("colder")
    print("")
    
  elif guess_difference < previous_guess_difference:
    print("warmer")
    print("")

  elif previous_guess_difference < 10:
    print("Hot!")
    print("")
    
  previous_guess_difference = guess_difference
