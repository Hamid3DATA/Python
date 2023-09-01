import os

the_word = "valorant"
word_length = len(the_word)
hearts = 5
Game = True
hint_count = 0


def print_hearts():
    for x in range(hearts):
        print(end="♡")


while Game:
    answer = input("The word is " + str(word_length) + " characters long, you have " + str(hearts) + " tries left."
                   "\nIf you need any hints type 'Hint' (3rd hint is the word itself). Hints used: " + str(hint_count) +
                   "\nIf you give up, type 'Exit' ")

    if answer:
        os.system('cls')

    if answer.lower() == "hint" and hint_count == 0:
        print("*The word is a name of a game*")
        hint_count += 1

    elif answer.lower() == "hint" and hint_count == 1:
        print("*The game is made by Riot Games*")
        hint_count += 1

    elif answer.lower() == "hint" and hint_count == 2:
        print("*The word is Valorant*")
        hint_count += 1

    if answer.lower() == the_word and hint_count == 3:
        print("You Won... but... you used all the hints, so it is not that impressive...")
        Game = False

    elif answer.lower() == the_word:
        print("Congratulations, you have won!\nThe word was indeed Valorant\nYou have used " + str(hint_count) +
              " hints.\nYou have " + str(hearts) + " tries left")
        Game = False

    if answer.lower() != the_word and answer.lower() != "exit" and answer.lower() != "hint":
        hearts -= 1
        print("Hearts left: " + str(hearts))
        if hearts == 0:
            print("Sadly, you did not guess the word...\nYou have used " + str(hint_count) + " hints")
            Game = False

    if answer.lower() == "exit":
        Game = False
