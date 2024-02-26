import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("Welcome to Rock, Paper, Scissors!")
while True:
    playerchoice = input("Enter your choice: ")
    player = int(playerchoice)

    if player < 1 or player > 3:
        print("Invalid choice")
        sys.exit()

    computer = random.randint(1, 3)

    if player == computer:
        print("It's a tie!")
    elif player == RPS.ROCK.value and computer == RPS.SCISSORS.value:
        print("You win! Rock beats Scissors")
    elif player == RPS.PAPER.value and computer == RPS.ROCK.value:
        print("You win! Paper beats Rock")
    elif player == RPS.SCISSORS.value and computer == RPS.PAPER.value:
        print("You win! Scissors beats Paper")

    playagain = input("Enter q to quit or any other key to play again: ")
    if playagain.lower() == "q":
        print("Thanks for playing!")
        sys.exit("Goodbye!")
