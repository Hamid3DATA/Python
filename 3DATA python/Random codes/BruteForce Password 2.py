from multiprocessing import Process
import time

password = input("Input your password: ")
start = time.time()
hash_password = hash(password)

print(hash_password)

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"
]

letters1 = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
]

letters2 = [
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

numbers = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]


def loop_a():
    letter1 = 0
    letter2 = 0
    letter3 = 0
    number1 = 0
    number2 = 0
    number3 = 0
    for x in letters1:
        letter1_password = letters1[letter1]
        letter1 += 1
        letter2 = 0
        for y in alphabet:
            letter2_password = alphabet[letter2]
            letter2 += 1
            letter3 = 0
            for z in alphabet:
                letter3_password = alphabet[letter3]
                letter3 += 1
                number1 = 0
                for a in numbers:
                    number1_password = numbers[number1]
                    number1 += 1
                    number2 = 0
                    for b in numbers:
                        number2_password = numbers[number2]
                        number2 += 1
                        number3 = 0
                        for c in numbers:
                            number3_password = numbers[number3]
                            number3 += 1
                            letter_half = letter1_password + letter2_password + letter3_password
                            number_half = f"{number1_password}{number2_password}{number3_password}"
                            password_guess = f"{letter_half}{number_half}"
                            password_guess_hash = hash(password_guess)
                            if password_guess_hash == hash_password:
                                end = time.time()
                                print(f"the password is {password_guess}")
                                print(f"the password hash is {password_guess_hash}")
                                print(f"it took: {end - start} sec")


def loop_b():
    letter4 = 0
    letter5 = 0
    letter6 = 0
    number4 = 0
    number5 = 0
    number6 = 0
    for x in letters2:
        letter4_password = letters2[letter4]
        letter4 += 1
        letter5 = 0
        for y in alphabet:
            letter5_password = alphabet[letter5]
            letter5 += 1
            letter6 = 0
            for z in alphabet:
                letter6_password = alphabet[letter6]
                letter6 += 1
                number4 = 0
                for a in numbers:
                    number4_password = numbers[number4]
                    number4 += 1
                    number5 = 0
                    for b in numbers:
                        number5_password = numbers[number5]
                        number5 += 1
                        number6 = 0
                        for c in numbers:
                            number6_password = numbers[number6]
                            number6 += 1
                            letter_half1 = letter4_password + letter5_password + letter6_password
                            number_half1 = f"{number4_password}{number5_password}{number6_password}"
                            password_guess1 = f"{letter_half1}{number_half1}"
                            password_guess_hash1 = hash(password_guess1)
                            if password_guess_hash1 == hash_password:
                                end = time.time()
                                print(f"the password is {password_guess1}")
                                print(f"the password hash is {password_guess_hash1}")
                                print(f"it took: {end - start} sec")


Process(target=loop_a())
Process(target=loop_b())
