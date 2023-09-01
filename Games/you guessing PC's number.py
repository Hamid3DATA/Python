import random
pc = (random.randrange(1, 10))
print("Guess the number i have chosen! (from 1 to 10)")
player = int(input())
if player == pc:
    print("Correct, you have won!")
else:
    print("Sorry, you have lost, my number was", pc)
