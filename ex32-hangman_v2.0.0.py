#!/usr/bin/python3

##########################################################################
#
#                    Exercise 32 - Hangman
#                        revision 2
#                        Jan 9, 2018
#                        By: a_aramini
#
# http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
#
# You will need the "sowpods.txt" file in order for the random word
# generation (and game) to work. You can download it here:
#
# http://norvig.com/ngrams/sowpods.txt
#
# (The file is approximately 3MB)
#
# Save the sowpods.txt file in the same directory as this python script
# then run this script to play the game.
#
##########################################################################

import random
import string
import sys
import os

def pick_word():
    with open('sowpods.txt', 'r') as f:
        line = random.choice(f.readlines()).strip()
    return line

def clear_screen():
    if sys.platform  == 'win32':
        clear = 'cls' # Windows/DOS
    else:
        clear = 'clear' # Unix/Linux/Mac
    return clear

def display_game(guesses_left, correct_letters, guessed):
    # Clear the screen and then print out the text and ASCII art for a cleaner
    # presentation to the user (prevents scrolling the screen)
    os.system(clear_screen())

    print (" " * 10 + "*" * 7 + "\n")
    print (" " * 10 + "HANGMAN\n")
    print (" " * 10 + "*" * 7)
    print ("\n\n" + "\n".join(graphics[guesses_left]))
    print ("\n" * 4 + " " * 5 + ' '.join(correct_letters) + "\n\n")
    #print (" " * 2 + word + "\n" * 2) # prints the "secret" word to guess for testing
    print ("\nGuesses left: %i \n" % guesses_left)
    print ("Letters Guessed: " + ' '.join(set(guessed)))

def replay():
    while True:
        ans = input("\nWould you like to play again? y or n?: ")
        if ans == "y":
            return start_game()
        elif ans == "n":
            game_exit()    

def game_exit():
    #If exiting normally, we don't care about the traceback
    # output just suppress that, call sys.exit with the
    # exit status (in this case a message) and exit cleanly
    sys.tracebacklimit=0
    print ("\n\n")
    sys.exit("Good Bye!\n\n")

def start_game():
    word = pick_word()
    
    guesses_left = 6 # Set the total number of guesses allowed
    correct_letters = list("_" * len(word))
    guessed = []

    display_game(guesses_left, correct_letters, guessed)

    while True:
        guess = input("\nEnter a letter to guess or type 'quit' to quit the game: ").upper()
        if guess == "QUIT": # don't forget that we are now working with upper-case letters
            game_exit()

        elif len(guess) != 1 or guess not in string.ascii_letters:
            print("Invalid input. Please Try Again.")
            continue

        if guess in guessed:
            print("You already guessed that letter! Try again")
            continue
        # Keep track of what letters have been guessed
        guessed.append(guess)

        # Check for a correct guess
        m = 0
        for i, letter in enumerate(word):
            if guess == word[i]:
                correct_letters[i] = word[i]
                m += 1
    
        if m == 0:
            guesses_left -= 1
        
        display_game(guesses_left, correct_letters, guessed)

        if guesses_left <= 0:
            print ("No guesses left, You lose!\n\n")
            print ("The word was: " + word + "\n\n")
            break

        if ''.join(correct_letters) == word:
            print ("\nCongratulations! You guessed the word!: " + word + "\n\n")
            break

        continue

    print ("Game Over!\n\n")
    # We're out of the loop now, so reset variables to allow a fresh game if
    # the user wants to play again, then call function that prompts the user
    # for another game
 
    del guessed
    
    replay()

if __name__ == "__main__":

    # Each element in graphics is a list with elements that represent one line
    # of an ascii art graphic, that will be printed out by the display_game()
    # function. They are then joined with a newline, ex. '\n'.join(graphics[i]),
    # so that they will be reassembled and printed out correctly.
    # 
    # The spacing and order matters here!
    #
    # Element 0 is the the last graphic we display because we are using
    # guesses_left which starts at 6 and is decremented for ever wrong
    # guess so the first time we print a graphic, we are printing graphics[6],
    # then graphics[5], then graphics[4]...etc each time we decrement the variable    

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
    start_game()