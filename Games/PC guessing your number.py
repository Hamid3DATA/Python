import random
guess = (random.randrange(0, 10))
print("Pick and write down a number between 1 and 10")
human = int(input())
print("now i will guess your number, are you ready? (1 is yes 2 is no)")
answer = int(input())
yes = 1
no = 2
if answer == yes:
    print("is your number", guess, "?")
if answer == no:
    print("ok, well... i guess i win, because you sort of gave up :)")
if human == guess:
    print("Yes, I Won!")
else:
    print("I guess i was wrong :(")
