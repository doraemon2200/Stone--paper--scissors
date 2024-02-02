import random

print("My name is AI. Let's play stone, paper and scissor")
name = input("Enter your name: ")
myscore = 0
compscore = 0

opt = ["stone", "paper", "scissors"]


while True:
    comp = random.choice(opt)
    mychance = input("So, what do you choose? ")
    if mychance == "quit":
        print(f"Thanks for coming here. Your score is {myscore} and my score is {compscore}")
        quit()
    if mychance == comp:
        print("tie")
    elif mychance == "stone" and comp == "scissors":
        print(f"{name} won")
        myscore += 1
    elif mychance == "paper" and comp == "stone":
        print(f"{name} won")
        myscore += 1
    elif mychance == "scissors" and comp == "paper":
        print(f"{name} won")
        myscore += 1
    else:
        print("AI won")
        compscore+=1
