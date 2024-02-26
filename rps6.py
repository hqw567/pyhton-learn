import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("Welcome to Rock, Paper, Scissors!\n")


def rps():
    game_count = 0
    user_win_count = 0
    computer_win_count = 0

    def play_rps():
        while True:
            playerchoice = input(
                "Enter your choice: \n1. Rock\n2. Paper\n3. Scissors\n"
            )
            if playerchoice in ["1", "2", "3"]:
                player = int(playerchoice)
                computer = random.randint(1, 3)

                def decide_winner(player, computer):
                    nonlocal user_win_count
                    nonlocal computer_win_count

                    if player == computer:
                        return "It's a tie!"
                    elif player == RPS.ROCK.value and computer == RPS.SCISSORS.value:
                        user_win_count += 1
                        return "You win! Rock beats Scissors"
                    elif player == RPS.PAPER.value and computer == RPS.ROCK.value:
                        user_win_count += 1
                        return "You win! Paper beats Rock"
                    elif player == RPS.SCISSORS.value and computer == RPS.PAPER.value:
                        user_win_count += 1
                        return "You win! Scissors beats Paper"
                    else:

                        computer_win_count += 1
                        return "You lose! Computer wins!"

                result = decide_winner(player, computer)
                print(result)
                nonlocal game_count

                game_count += 1
                print(f"Game count: {game_count}")
                print(f"You Win count: {user_win_count}")
                print(f"Computer Win count: {computer_win_count}")
                playagain = input("Enter q to quit or any other key to play again: ")
                if playagain.lower() == "q":
                    print("Thanks for playing!")
                    sys.exit("Goodbye!")
            else:
                print("Invalid choice")
                play_rps()

    return play_rps


start = rps()
start()
