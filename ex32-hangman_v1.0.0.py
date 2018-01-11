#!/usr/bin/python3

##########################################################################
#
#                    Exercise 32 - Hangman
#    http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
#
#         File Name:    ex32-hangman_v1.0.0.py
#    Python Version:    3.6.4
#              Date:    Jan 7, 2018
#                By:    a_aramini
#
# You will need the "sowpods.txt" file in order for the random word
# generation to work. You can download it here:
#
# http://norvig.com/ngrams/sowpods.txt
#
# (The file is approx 3MB)
#
# Save the sowpods.txt file in the same directory as this python script
# then run this script to play the game.
#
##########################################################################

import random
import string
import os
import sys

def pick_word():
    with open('sowpods.txt', 'r') as f:
        line = random.choice(f.readlines()).strip()
    return line

def clear_screen():
    if sys.platform  == 'win32':
        clear = 'cls'
    else:
        clear = 'clear'
    return clear

def draw_art(count, graphics):
    print ("\n\n" + "\n".join(graphics[count]))

def display_game(a, word, guessed, count, graphics):

    os.system(clear_screen())

    print (" " * 10 + "*" * 7 + "\n")
    print (" " * 10 + "HANGMAN\n")
    print (" " * 10 + "*" * 7)

    draw_art(count, graphics)

    print ("\n" * 4 + " " * 5 + ' '.join(a) + "\n\n")
    #print (" " * 2 + word + "\n" * 2)
    print ("\nGuesses left: %i \n" % count)
    print ("Letters Guessed: " + ' '.join(set(guessed)))

def check_guess(a, guess, word, guessed):
    match = False
    for i in range(len(word)):
        if guess == word[i]:
            a[i] = word[i]
            match = True
    return match

def replay():
    while True:
        a = input("\nWould you like to play again? y or n?: ")
        if a == "y":
            return play_game()
        elif a == "n":
            os._exit(1)    

def play_game():
    word = pick_word()
    a = list("_" * len(word))
    guessed = []
    count = 6 #len(word)

    display_game(a, word, guessed, count, graphics)

    while True:
        guess = input("\nEnter a letter to guess or type 'quit' to quit the game: ").upper()
        if guess == "QUIT":
            os._exit(1)
        if len(guess) != 1 or guess not in string.ascii_letters:
           print("Invalid input. Please Try Again.")
           continue

        if guess in guessed:
            print("You already guessed that letter! Try again")
            continue

        guessed.append(guess)

        if not check_guess(a, guess, word, guessed):
            count -= 1

        display_game(a, word, guessed, count, graphics)

        if count <= 0:
            print ("No guesses left, You lose!\n\n")
            print ("The word was: " + word + "\n\n")
            break

        if ''.join(a) == word:
            print ("\nCongratulations! You guessed the word!: " + word + "\n\n")
            break

        continue

    print ("Game Over!\n\n")

    replay()

if __name__ == "__main__":
    graphics = [
           ["     +--------------+        ", "     |              |        ", "     |              |        ",
            "     |              |        ", "     |           -------     ", "     |          | X   X |    ",
            "     |          |   x   |    ", "     |          |  xxx  |    ", "     |           -------     ",
            "     |              |        ", "     |              |        ", "     |             /|\       ",
            "     |            / | \      ", "     |              |        ", "     |             / \       ",
            "     |           _/   \_     ", "     |                       ", "     |                       ",
            "     |                       ", "-----------                  "],  

           ["     +--------------+        ", "     |              |        ", "     |              |        ",
            "     |              |        ", "     |           -------     ", "     |          | X   X |    ",
            "     |          |   x   |    ", "     |          |  xxx  |    ", "     |           -------     ",
            "     |              |        ", "     |              |        ", "     |             /|\       ",
            "     |            / | \      ", "     |              |        ", "     |             /         ",
            "     |           _/          ", "     |                       ", "     |                       ",
            "     |                       ", "-----------                  "],            

           ["     +--------------+        ", "     |              |        ", "     |              |        ",
            "     |              |        ", "     |           -------     ", "     |          | X   X |    ",
            "     |          |   x   |    ", "     |          |  xxx  |    ", "     |           -------     ",
            "     |              |        ", "     |              |        ", "     |             /|\       ",
            "     |            / | \      ", "     |                       ", "     |                       ",
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "-----------                  "],

           ["     +--------------+        ", "     |              |        ", "     |              |        ",
            "     |              |        ", "     |           -------     ", "     |          | X   X |    ",
            "     |          |   x   |    ", "     |          |  xxx  |    ", "     |           -------     ",
            "     |              |        ", "     |              |        ", "     |             / \       ",
            "     |            /   \      ", "     |                       ", "     |                       ",
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "-----------                  "],

           ["     +--------------+        ", "     |              |        ", "     |              |        ",
            "     |              |        ", "     |           -------     ", "     |          | X   X |    ",
            "     |          |   x   |    ", "     |          |  xxx  |    ", "     |           -------     ",
            "     |              |        ", "     |              |        ", "     |             /         ",
            "     |            /          ", "     |                       ", "     |                       ",
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "-----------                  "],

           ["     +--------------+        ", "     |              |        ", "     |              |        ",
            "     |              |        ", "     |           -------     ", "     |          | X   X |    ",
            "     |          |   x   |    ", "     |          |  xxx  |    ", "     |           -------     ",
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "-----------                  "],
    

           ["     +--------------+        ", "     |              |        ", "     |              |        ", 
            "     |              |        ", "     |                       ", "     |                       ", 
            "     |                       ", "     |                       ", "     |                       ", 
            "     |                       ", "     |                       ", "     |                       ", 
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "     |                       ", "     |                       ",
            "     |                       ", "-----------                  "]
]

    play_game()
