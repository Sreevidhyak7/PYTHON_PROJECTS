"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

import random
item_list = ["rock", "paper", "scissor"]

user_choice = input("Enter your move (Rock/Paper/Scissor) = ").lower()
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You win")

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")
