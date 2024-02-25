import sys
import random
from enum import Enum

count = 0

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

print("Welcome to Rock, Paper, Scissors!")

def play_rps():
  while True:
    playerchoice = input("""
    Enter your choice: 
    1. Rock
    2. Paper
    3. Scissors
    """)
    if playerchoice in ["1", "2", "3"]:
      player = int(playerchoice)
      computer = random.randint(1, 3)

      
      def decide_winner(player, computer):
        if(player == computer):
          return "It's a tie!"
        elif(player == RPS.ROCK.value and computer == RPS.SCISSORS.value):
          return "You win! Rock beats Scissors"
        elif(player == RPS.PAPER.value and computer == RPS.ROCK.value):
          return "You win! Paper beats Rock"
        elif(player == RPS.SCISSORS.value and computer == RPS.PAPER.value):
          return "You win! Scissors beats Paper"
        else:
          return "You lose! Computer wins!"
      result = decide_winner(player, computer)
      print(result)
      global count
      count += 1
      print(f"Game count: {count}")
      playagain = input("Enter q to quit or any other key to play again: ")
      if playagain.lower() == "q":
        print("Thanks for playing!")  
        sys.exit("Goodbye!")
    else:
      print("Invalid choice")
      play_rps()

play_rps()
