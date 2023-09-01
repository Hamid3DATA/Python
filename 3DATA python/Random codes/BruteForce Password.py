password = input("Input your password: ")

letter1 = 0
letter2 = 0
letter3 = 0

number1 = 0
number2 = 0
number3 = 0

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in letters:
    letter1_password = (letters[letter1])
    letter1 += 1
    letter2 = 0
    for y in letters:
        letter2_password = (letters[letter2])
        letter2 += 1
        letter3 = 0
        for z in letters:
            letter3_password = (letters[letter3])
            letter3 += 1
            number1 = 0
            for a in numbers:
                number1_password = (numbers[number1])
                number1 += 1
                number2 = 0
                for b in numbers:
                    number2_password = (numbers[number2])
                    number2 += 1
                    number3 = 0
                    for c in numbers:
                        number3_password = (numbers[number3])
                        number3 += 1
                        letter_password = (letter1_password + letter2_password + letter3_password)
                        number_password = f"{number1_password}{number2_password}{number3_password}"
                        password_guess = f"{letter_password}{number_password}"
                        if password_guess == password:
                            print(f"the password is {password_guess}")
