import random

choices = ["rock", "paper", "scissors"]
rock_paper_scissors = random.choice(choices)

print("rock, paper, scissors, shoot!")
user = input()

if user == rock_paper_scissors:
    print("pc chose", rock_paper_scissors)
    print("it is a tie!")

if user == "rock" and rock_paper_scissors == "paper":
    print("pc chose", rock_paper_scissors)
    print("you lost!")
if user == "rock" and rock_paper_scissors == "scissors":
    print("pc chose", rock_paper_scissors)
    print("you won!")

if user == "paper" and rock_paper_scissors == "scissors":
    print("pc chose", rock_paper_scissors)
    print("you lost!")
if user == "paper" and rock_paper_scissors == "rock":
    print("pc chose", rock_paper_scissors)
    print("you won!")

if user == "scissors" and rock_paper_scissors == "rock":
    print("pc chose", rock_paper_scissors)
    print("you lost!")
if user == "scissors" and rock_paper_scissors == "paper":
    print("pc chose", rock_paper_scissors)
    print("you won!")
