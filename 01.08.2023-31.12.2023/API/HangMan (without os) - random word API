import requests
import json

url = "https://random-word-api.herokuapp.com/word"
r = requests.request("GET", url)
word = json.dumps(r.json())
word = word.replace("[", "").replace("]", "").replace('"', '')

word_length = len(word)
word_list = list(word)
tries = 10
game = True
stuff = "_" * word_length
stuff_list = list(stuff)
letter_indices = []
letters_used = []

# https://www.freecodecamp.org/news/python-find-in-list-how-to-find-the-index-of-an-item-or-element-in-a-list/

while True:

    answer1 = input("If you want to know the rules of the game type 'rules' \nIf you want to give up type 'exit' \nIf you want to start type 'start'")
    print("")

    if answer1.lower() == "rules":

        print("*The rules are simple, you have to guess the word, that is " + str(word_length) + " characters long, "
            "you have " + str(tries) + " tries, you can also guess one letter at a time.")
        print("")

    elif answer1.lower() == "exit":
        exit()

    elif answer1.lower() == "start":
        print("This is Hangman, you have " + str(tries) + " tries total.")
        print(stuff_list)
        break

if answer1.lower() == "start":

    while game:

        answer = input("Guess:")
        
        if answer.lower() != word and len(answer) > 1 or answer.lower() != word and len(answer) == 1 and answer not in word_list:
            tries -= 1
            for x in range(2):
                print("")
            
            if answer.lower() not in word and len(answer.lower()) < 2:
                if answer not in letters_used:
                    letters_used.append(answer.lower())
            
            print(''.join(stuff_list))
            print("Letters used: " + str(letters_used))
            print("Tries left: " + str(tries))

        if answer:
            letter_indices.clear()

        if tries == 0:
            for x in range(20):
                print("")

            print("Game Over!")
            print("The word was: " + word)

            game = False

        if answer.lower() in word and len(answer.lower()) < 2:

            for x in range(len(word_list)):
                if word_list[x] == answer.lower():
                    letter_indices.append(x)

            for y in range(len(letter_indices)):
                stuff_list[letter_indices[y]] = answer.lower()

                for x in range(2):
                    print("")

                print(''.join(stuff_list))
                print("Letters used: " + str(letters_used))
                print("Tries left: " + str(tries))

        if answer.lower() == word or ''.join(stuff_list) == word:

            for x in range(20):
                print("")

            print("Congratulations, you have won! You had " + str(tries) +
                " try(tries) left")
            print("The word was: " + word)

            game = False
