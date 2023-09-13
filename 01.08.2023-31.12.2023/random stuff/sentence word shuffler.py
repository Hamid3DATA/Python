import random

print("Welcome to my Word/Sentence_Project! :)")

user_sentence = input("Put in your word/sentence: ")

sentence_list = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_signs = [",", ".", ";", ":", "<", ">", "*", "+" "=", "!", "?", "/", "'", '"', "-", "_", "–", "—", "(", ")", "[", "]", "%", "&" "@", "#", "\\", "|", "¤", "$", "€" ]


status = False

letters_combined = ""
var1 = ""
var2 = ""

for x in user_sentence:

    for y in alphabet:

        if x in y:
            letters_combined += x
            status = True
            break
        
        if x is " ":
            sentence_list.append(letters_combined)
            letters_combined = ""
            sentence_list.append(x)
            status = True
            break
        
    if status == False:

        for h in upper_alphabet:

            if x in h:
                letters_combined += x
                status = True
                break
            
    
    if status == False:
         
         for z in special_signs:

            if x in z:
                sentence_list.append(letters_combined)
                letters_combined = ""
                sentence_list.append(x)
                break

    status = False

    


sentence_list.append(letters_combined)

letters_combined = ""

fixed_sentence_list = list(filter(None, sentence_list))

final_sentence_list = []

for x in fixed_sentence_list:

    if len(x) > 3:

        final_sentence_list.append(x[0])

        var1 = x[1:-1]
        var2 = ''.join(random.sample(var1,len(var1)))

        final_sentence_list.append(var2)
        final_sentence_list.append(x[-1])

        var1 = ""
        var2 = ""

    else:

        final_sentence_list.append(x)


the_final_sentence_list = "".join(final_sentence_list)

print(the_final_sentence_list)
