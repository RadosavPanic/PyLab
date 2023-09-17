# Hangman game
"""
Program random chooses one word from a static list, then it
begin a process of guessing. Placeholder for non-right letters
is underscore letter, while right guessed letters are replaced
with underscore.
"""

import random
from hangman_game_utils import print_welcome_message

print_welcome_message()

guessing_words = [
    "monitor", "keyboard", "processor",
    "graphics", "motherboard", "memory",
    "mouse", "ethernet", "webcam", "headphones"]

hidden_word = random.choice(guessing_words)

numGuessesLeft = len(hidden_word) + 5
numRightGuesses = 0

rightGuessesList = ["_"] * len(hidden_word)

print(f"Hidden word has {len(hidden_word)} letters")

while numGuessesLeft > 0:
    if numRightGuesses == len(hidden_word):
        break
    counter = 0
    letterInput = input(f"Number of guesses left: {numGuessesLeft}.\nEnter a letter: ")
    for letter in hidden_word:
        if letter == letterInput[0].lower():
            rightGuessesList[counter] = letter
            numRightGuesses += 1
        counter += 1
    numGuessesLeft -= 1
    print("Hidden word: " + "".join(rightGuessesList))
if numGuessesLeft:
    print("You won!")
else:
    print("You lost!")
