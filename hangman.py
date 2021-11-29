import random
import time
import sys

print("Welcome to Hangman!")
print("Made by @exrayy.")
time.sleep(2)

guesses = ""
turns = 5
failed = 0
x = 1
words = [""]

#Themes
themes = ["Sports", "Music Genres", "Breakfast", "Mammals", "Horror Films", "Continents", "FPS Games", "Cities"]
theme = (random.choice(themes))

print("The theme is:", theme)

if theme == "Sports":
    words = ["football", "rugby", "golf", "tennis", "basketball", "baseball"]
elif theme == "Music Genres":
    words = ["jazz", "hiphop", "edm", "rock", "indie", "pop", "classical"]
elif theme == "Breakfast":
    words = ["granola", "fruit", "bacon", "yoghurt", "coffee", "toast"]
elif theme == "Mammals":
    words = ["lion", "tiger", "zebra", "whale", "monkey", "bear", "rabbit"]
elif theme == "Horror Films":
    words = ["it", "the conjuring", "psycho", "alien", "the exorcist", "insidious"]
elif theme == "Continents":
    words = ["antarctica", "europe", "americas", "oceania", "asia", "africa"]
elif theme == "FPS Games":
    words = ["overwatch", "apex legends", "csgo", "valorant", "halo"]
elif theme == "Cities":
    words = ["london", "new york", "beijing", "sydney", "tokyo", "munich", "oslo"]


word = (random.choice(words))
time.sleep(2)
                
#Game Loop
while (turns >= 0):
    guess = input("Enter a letter: ")
    guesses += guess

    if guess == word:
        print("You won! The word was:", word)
        play_again = input("Play again? Y or N?")
        if play_again == "Y":
            turns = 5
         else:
             sys.exit()
            
    if guess not in word:
        print(guess,"is not in the word.")
        print("You have", turns, "guesses remaining.")
        turns -= 1

    for char in word:
            if char in guesses:
                print(char)
            else:
                print("-")
        
    if guess in word:
        print(guess.upper(),"is in the word!")
        print("You have", turns, "guesses remaining.")

    if turns == 0:
        print("You lost, better luck next time!\nThe word was:",word)
        time.sleep(2)

    if turns == 0:
        play_again = input("Would you like to play again? Y- Yes, N-No.")
        if play_again == "Y":
            guesses = 5
        elif play_again == "N":
            sys.exit()
            

