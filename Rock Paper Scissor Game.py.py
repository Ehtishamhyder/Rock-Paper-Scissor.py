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

import random
item_list = ["rock", "paper", "scissor"]

your_choice = input("Enter your choice = rock, paper, scissor=")
ehtisham_choice = random.choice(item_list)

print(f"Ehtisham's choice: {ehtisham_choice}", f"your's choice: {your_choice}")

if your_choice == ehtisham_choice:
    print ("Tie")

elif your_choice == "rock":
   if ehtisham_choice == "scissor":
       print ("You win")
   else:
       print ("Ehtisham wins")

elif your_choice == "paper":
    if ehtisham_choice == "rock":
       print ("You win")
    else:
        print ("Ehtisham wins")

elif your_choice == "scissor":
    if ehtisham_choice == "rock":
       print ("Ehtisham wins")
    else:
      print ("You win")




