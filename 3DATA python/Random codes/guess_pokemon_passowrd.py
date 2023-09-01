import time

password = input("Input your password (7 characters): ")
start = time.time()
hash_password = hash(password)

print(hash_password)

letter1 = 0
letter2 = 0
letter3 = 0
letter4 = 0
letter5 = 0
letter6 = 0
letter7 = 0

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"
]

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
            letter4 = 0
            for a in letters:
                letter4_password = (letters[letter4])
                letter4 += 1
                letter5 = 0
                for b in letters:
                    letter5_password = (letters[letter5])
                    letter5 += 1
                    letter6 = 0
                    for c in letters:
                        letter6_password = (letters[letter6])
                        letter6 += 1
                        letter7 = 0
                        for d in letters:
                            letter7_password = (letters[letter7])
                            letter7 += 1
                            letter_half = (letter1_password + letter2_password + letter3_password + letter4_password
                                           + letter5_password + letter6_password + letter7_password)

                            if letter_half == password:
                                end = time.time()
                                print(letter_half)
                                print(f"it took: {end - start} sec")
                                break
