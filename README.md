

Hangman word guessing game with ASCII art graphics v2.0.0
Language: Python 3/Python console (sorry not a modern GUI)
Released: Jan 9, 2018
Files: ex32-hangman_v2.0.0.py, sowpods.zip

ex32-hangman_v2.0.0.py - The Hangman game script/source code

(ex32 stands for exercise 32 on PracticePython.org (http://www.practicepython.org/exercise/2017/01/10/32-hangman.html) and has nothing to do with 32-bit or win32 exe, etc. It was written on Windows 7 using Python 3.6.4 and NotePad++v7.5.4.

sowpods.zip - contains a 2.94MB text file, sowpods.txt, that the python script needs to work.

sowpods.txt is just a text file containing Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word. The original source for this file is:
http://norvig.com/ngrams/sowpods.txt

Extract sowpods.txt from the zip and place ex32-hangman_v2.0.0.py and sowpods.txt in the same directory before running the ex32-hangman_v2.0.0.py file.

Installation:

For the game to run without modifying the code, you need to have Python 3 installed. It is also dependent upon 4 standard Python libraries: os, sys, random and string.

In this version:

Refactored the code a bit to make it cleaner and more readable. Added comments for clarity. Should be easier to follow the code...(less spaghetti, more ravioli).
