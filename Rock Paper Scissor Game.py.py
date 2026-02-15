"""
workflow:
1- input from your(rock,paper,scissor)
2- ehtisham choice(randomly choose but not conditionally)
3- Result print who is winner

Cases:
rock - paper = paper win
rock - scissor = rock win
rock - rock = tie
scissor vs paper = scissor win
scissor vs rock = rock win
scissor vs scissor = tie
paper vs paper = tie
paper vs rock = paper win
paper vs scissor = scissor win
"""

print("Welcome to the Rock Paper Scissor Game!")
import random
item_list = ["rock", "paper", "scissor"]

your_choice = input("Enter your choice (rock, paper, scissor):")
computer_choice = random.choice(item_list)

print(f"Computer choice: {computer_choice}")
print(f"your choice: {your_choice}")

if your_choice == computer_choice:
    print ("Tie")

elif your_choice == "rock":
   if computer_choice == "scissor":
       print ("You win")
   else:
       print ("You lose")

elif your_choice == "paper":
    if computer_choice == "rock":
       print ("You win")
    else:
        print ("You lose")

elif your_choice == "scissor":
    if computer_choice == "rock":
       print ("You lose")
    else:
      print ("You win")




