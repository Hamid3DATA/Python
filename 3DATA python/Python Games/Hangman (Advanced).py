import os

word = "applied"
word_length = len(word)
word_list = list(word)
hint_count = 0
tries = 10
game = True
stuff = "_" * word_length
stuff_list = list(stuff)
letter_indices = []
letters_used = []

# https://www.freecodecamp.org/news/python-find-in-list-how-to-find-the-index-of-an-item-or-element-in-a-list/

print("This is Hangman, you have " + str(tries) + " tries total.")

while game:
    answer = input("If you want to know the rules of the game type 'rules' \nIf you need hints type 'hint'\nIf you want to give up type 'exit'\nAnswer:")

    if answer.lower() != word and answer.lower() != "hint" and answer.lower() != "rules" and len(answer.lower()) > 1 or answer.lower() != word and answer.lower() != "hint" and answer.lower() != "rules" and len(answer.lower()) == 1:
        tries -= 1

    if answer and answer != "exit":
        os.system('cls')
        letter_indices.clear()

        if tries == 0:
            os.system('cls')
            print("Game Over!")
            print("The word was: " + word)
            game = False

        if answer.lower() not in word and len(answer.lower()) < 2:
            if answer not in letters_used:
                letters_used.append(answer.lower())

        if answer.lower() in word and len(answer.lower()) < 2:
            for x in range(len(word_list)):
                if word_list[x] == answer.lower():
                    letter_indices.append(x)
            for y in range(len(letter_indices)):
                stuff_list[letter_indices[y]] = answer.lower()
        print(''.join(stuff_list))
        print("Letters used: " + str(letters_used))
        print("Tries left: " + str(tries))

    if answer.lower() == "rules":
        print("*The rules are simple, you have to guess the word, that is " + str(word_length) + " characters long, "
              "you have " + str(tries) + " tries, you can also guess one letter at a time(you have " + str(word_length) +
              " hints total)")

    if answer.lower() == "hint":
        hint_count += 1
        print("*Hint nr. " + str(hint_count) + "*")

    if answer.lower() == word and hint_count == word_length or answer.lower() == word and hint_count == word_length - 1 or ''.join(stuff_list) == word and hint_count == word_length or ''.join(stuff_list) == word and hint_count == word_length - 1:
        print("You won, but... it seems like you used a lot of hints... so... not that impressive...")
        print("Hints used: " + str(hint_count))
        game = False

    elif answer.lower() == word and hint_count > word_length or ''.join(stuff_list) == word and hint_count > word_length:
        print("I don't know what you were trying to do...")
        print("You literally used more hints than there are letters in the word... like... why... or how....")
        print("Hints used: " + str(hint_count))
        game = False

    elif answer.lower() == word or ''.join(stuff_list) == word:
        os.system('cls')
        print("Congratulations, you have won! You used " + str(hint_count) + " hints, and you had " + str(tries) +
              " try(tries) left")
        print("The word was: " + word)
        game = False

    if answer.lower() == "exit":
        game = False
