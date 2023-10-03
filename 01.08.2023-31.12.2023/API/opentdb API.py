import requests
import json
import random

game = True
points = 0

help0 = 0
help1 = 0
help2 = 0
help3 = 0
help4 = 0
help5 = 0
help6 = 0
help7 = 0
help8 = 0
help9 = 0


endpoint = "https://opentdb.com/api.php?amount=10"

r = requests.request("GET", endpoint)

for x in range(10):
    exec(f'question_category{x} = r.json()["results"][x]["category"]')

for x in range(10):
  exec(f'question_type{x} = r.json()["results"][x]["type"]')

for x in range(10):
  exec(f'question_difficulty{x} = question1_difficulty = r.json()["results"][x]["difficulty"]')

for x in range(10):
  exec(f'question{x} = r.json()["results"][x]["question"]')

for x in range(10):
  exec(f'question_correct{x} = r.json()["results"][x]["correct_answer"]')



if question_type0 == "multiple":
  answers0 = r.json()["results"][0]["incorrect_answers"]
  answers0.append(r.json()["results"][0]["correct_answer"])
  random.shuffle(answers0)
else:
  help0 = 1


if question_type1 == "multiple":
  answers1 = r.json()["results"][1]["incorrect_answers"]
  answers1.append(r.json()["results"][1]["correct_answer"])
  random.shuffle(answers1)
else:
  help1 = 1
  

if question_type2 == "multiple":
  answers2 = r.json()["results"][2]["incorrect_answers"]
  answers2.append(r.json()["results"][2]["correct_answer"])
  random.shuffle(answers2)
else:
  help2 = 1


if question_type3 == "multiple":
  answers3 = r.json()["results"][3]["incorrect_answers"]
  answers3.append(r.json()["results"][3]["correct_answer"])
  random.shuffle(answers3)
else:
  help3 = 1

if question_type4 == "multiple":
  answers4 = r.json()["results"][4]["incorrect_answers"]
  answers4.append(r.json()["results"][4]["correct_answer"])
  random.shuffle(answers4)
else:
  help4 = 1
  
if question_type5 == "multiple":
  answers5 = r.json()["results"][5]["incorrect_answers"]
  answers5.append(r.json()["results"][5]["correct_answer"])
  random.shuffle(answers5)
else:
  help5 = 1
  
if question_type6 == "multiple":
  answers6 = r.json()["results"][6]["incorrect_answers"]
  answers6.append(r.json()["results"][6]["correct_answer"])
  random.shuffle(answers6)
else:
  help6 = 1
  
if question_type7 == "multiple":
  answers7 = r.json()["results"][7]["incorrect_answers"]
  answers7.append(r.json()["results"][7]["correct_answer"])
  random.shuffle(answers7)
else:
  help7 = 1
  
if question_type8 == "multiple":
  answers8 = r.json()["results"][8]["incorrect_answers"]
  answers8.append(r.json()["results"][8]["correct_answer"])
  random.shuffle(answers8)
else:
  help8 = 1
  
if question_type9 == "multiple":
  answers9 = r.json()["results"][9]["incorrect_answers"]
  answers9.append(r.json()["results"][9]["correct_answer"])
  random.shuffle(answers9)
else:
  help9 = 1


print("There are 10 random trivia questions all you need to do is answer correctly to get points")
print()
print("NOTE! Spelling is super important, even if you just miss a comma(,) the answer will be incorrect. Which means that the easiest way to answer is to copy and paste the desired answer!")
print("press enter to start!")
input()

while game:
  
  print("category: " + question_category0)
  print("type: " + question_type0)
  print("difficulty: " + question_difficulty0)
  print("question: " + question0)
  
  if help0 == 0:
    print("answers: " + str(answers0))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct0.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct0)
    print("")
  
  
  
  print("category: " + question_category1)
  print("type: " + question_type1)
  print("difficulty: " + question_difficulty1)
  print("question: " + question1)
  
  if help1 == 0:
    print("answers: " + str(answers1))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct1.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct1)
    print("")
    
  
  print("category: " + question_category2)
  print("type: " + question_type2)
  print("difficulty: " + question_difficulty2)
  print("question: " + question2)
  
  if help2 == 0:
    print("answers: " + str(answers2))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct2.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct2)
    print("")
  
  
  
  print("category: " + question_category3)
  print("type: " + question_type3)
  print("difficulty: " + question_difficulty3)
  print("question: " + question3)
  
  if help3 == 0:
    print("answers: " + str(answers3))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct3.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct3)
    print("")
  
  
  
  print("category: " + question_category4)
  print("type: " + question_type4)
  print("difficulty: " + question_difficulty4)
  print("question: " + question4)
  
  if help4 == 0:
    print("answers: " + str(answers4))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct4.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct4)
    print("")
  
  
  
  print("category: " + question_category5)
  print("type: " + question_type5)
  print("difficulty: " + question_difficulty5)
  print("question: " + question5)
  
  if help5 == 0:
    print("answers: " + str(answers5))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct5.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct5)
    print("")
  
  
  
  print("category: " + question_category6)
  print("type: " + question_type6)
  print("difficulty: " + question_difficulty6)
  print("question: " + question6)
  
  if help6 == 0:
    print("answers: " + str(answers6))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct6.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct6)
    print("")
  
  
  
  print("category: " + question_category7)
  print("type: " + question_type7)
  print("difficulty: " + question_difficulty7)
  print("question: " + question7)
  
  if help7 == 0:
    print("answers: " + str(answers7))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct7.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct7)
    print("")
  
  
  
  print("category: " + question_category8)
  print("type: " + question_type8)
  print("difficulty: " + question_difficulty8)
  print("question: " + question8)
  
  if help8 == 0:
    print("answers: " + str(answers8))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct8.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct8)
    print("")
  
  
  print("category: " + question_category9)
  print("type: " + question_type9)
  print("difficulty: " + question_difficulty9)
  print("question: " + question9)
  
  if help9 == 0:
    print("answers: " + str(answers9))
  else:
    print("True or False?")
  
  answer = input("Answer: ")
  
  if answer.lower() == question_correct9.lower():
    print("Correct! +1 point")
    points += 1
    print("")
  else:
    print("incorrect! +0 point")
    print(question_correct9)
    print("")
  
  print("You have ended the trivia with " + str(points) + " points")
  break
