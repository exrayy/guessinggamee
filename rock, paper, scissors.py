import random
import time

print("Welcome to Rock, Paper, Scissors.")
print("Made by @exrayy.")
time.sleep(2)

wins = False
options = ["rock", "paper", "scissors"]
bot_action = (random.choice(options))

user_action = input("\nRock, paper or scissors? ")

while True:
    if user_action == bot_action:
        print(f"Both players selected",user_action,". It's a tie!")
    elif user_action == "rock":
        if bot_action == "scissors":
            print("Rock obliterates scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if bot_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if bot_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Would you like to play again? y/n? ")
    if play_again.lower() != "y":
        break
