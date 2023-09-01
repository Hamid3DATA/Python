from multiprocessing import Process
import time

password = input("Input your password: ")
hash_password = hash(password)
start = time.time()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def loop_a():
    letter1 = 0
    letter2 = 0
    letter3 = 0
    number1 = 0
    number2 = 0
    number3 = 0
    for x in letters:
        letter_1 = letters[letter1]
        letter1 += 1
        letter2 = 0
        for y in letters:
            letter_2 = letters[letter2]
            letter2 += 1
            letter3 = 0
            for z in letters:
                letter_3 = letters[letter3]
                letter3 += 1
                number1 = 0
                for a in numbers:
                    number_1 = numbers[number1]
                    number1 += 1
                    number2 = 0
                    for b in numbers:
                        number_2 = numbers[number2]
                        number2 += 1
                        number3 = 0
                        for c in numbers:
                            number_3 = numbers[number3]
                            number3 += 1
                            password_guess = f"{letter_1}{letter_2}{letter_3}{number_1}{number_2}{number_3}"
                            password_guess_hash = hash(password_guess)
                            if password_guess_hash == hash_password:
                                end = time.time()
                                print(f"the password is {password_guess}")
                                print(f"the password hash is {password_guess_hash}")
                                print(f"it took: {end - start} sec")


Process(target=loop_a())
