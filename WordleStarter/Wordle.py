# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS

from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    sec = random.choice(FIVE_LETTER_WORDS)  # choose random word from list 

    def enter_action(s):  # word letter you enter 
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("That's not a valid word.")
            return
        guessed_letters = list(s)

        current_row = gw.get_current_row()  

        # Initialize variables to keep track of correct, present, and missing letters
        correct_letters = []
        present_letters = []
        missing_letters = []

        # Check each letter in the word
        for col in range(len(sec)):
            letter = sec[col]
            # so if position of Secret word letter == position of guessed letter then CORRECT LETTER 
            guessed_letter = guessed_letters[col].lower()
            
            if guessed_letter == letter:  # if guessed letter is in the correct position
                correct_letters.append(col)
            elif guessed_letter in sec:  # if guessed letter is present in the word but in the wrong position
                present_letters.append(col)
            else:  # else if guessed letter not in the word
                missing_letters.append(col)


        # Update colors based on correct, present, and missing letters
        for col in range(len(sec)):
            if col in correct_letters:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
            elif col in present_letters:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)

        # Check if the user has correctly guessed all five letters
        if len(correct_letters) == N_COLS:
            print("Congratulations! You guessed the word correctly.")

        # Move on to the next row
        # Get the current row from WordleGraphics
        gw.set_current_row(current_row + 1)

        # Print statements for debugging
        # print(f"sec word: {sec}")
        # print(f"Correct Letters: {correct_letters}")
        # print(f"Present Letters: {present_letters}")
        # print(f"Missing Letters: {missing_letters}")

    

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()

