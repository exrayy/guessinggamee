import random
import time

print("Welcome to Number Guess!")
print("Made by @exrayy.")
time.sleep(1)

num = random.randint(1, 10)
tries = 3
x = 1

while (x <= 5):
    guess = int(input("Guess a number between 1-10: "))
    if guess > num:
        print("Lower!")
        tries -= 1
        print("You have", tries, "trie(s) left!")
    elif guess < num:
        print("Higher!")
        tries -= 1
        print("You have", tries, "trie(s) left!")
    elif guess > 10:
        print("Invalid!")
        tries -= 1
        print("You have", tries, "trie(s) left!")
    elif guess == num:
        print("You got it!")
        time.sleep(1)
        play_again = input("Would you like to play again? Y or N?")
        if play_again == "N":
            break
        if play_again == "Y":
            tries = 3
            
    if tries == 0:
        print("Hard luck! You're out of tries.")
        time.sleep(1)
        play_again = input("Would you like to play again? Y or N?")
        if play_again == "N":
            break
        if play_again == "Y":
            tries = 3
    if tries == 0:
        break
        
    

        


        

