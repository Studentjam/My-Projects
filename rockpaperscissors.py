import random
import sys

from enum import Enum 

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3



print ("")

playerinput = input("Enter...\n1 for Rock, \n2 for paper, or \n3 for scissors:\n\n")

player = int(playerinput)

if player < 1 | player > 3:
    sys.exit ("Please enter 1, 2, or 3.")

computerinput = random.choice("123")

computer = int(computerinput)
print("")
print("You picked "+ playerinput + ".")
print("Game picked "+ computerinput + ".")
print(" ")

if player == 1 and computer == 3:
    print("You won!")
elif player == 2 and computer == 1:
    print ("Game won!")
elif player == 3 and computer == 2:
    print("Game won!")
elif player == computer:
    print("It\s a Tie!")
else:
    print("You won!")