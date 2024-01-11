import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleDictionary import myList

def wordle():

    def enter_action(s):  # word letter you enter 
        sec = random.choice(myList)  # choose random word from list 
        guessed_letters = list(s)

        # Initialize variables to keep track of correct, present, and missing letters
        correct_letters = []
        present_letters = []
        missing_letters = []

        # Check each letter in the word
        for col in range(len(sec)):
            letter = sec[col]
            # so if position of Secret word letter == position of guessed letter then CORRECT LETTER 
            guessed_letter = guessed_letters[col]
            if guessed_letter == letter:  # if guessed letter is in the correct position
                correct_letters.append(col)
            elif guessed_letter in sec:  # if guessed letter is present in the word but in the wrong position
                present_letters.append(col)
            else:  # else if guessed letter not in the word
                missing_letters.append(col)

        # Print the guessed word and the results
        print(f"Guessed Word: {''.join(guessed_letters)}")
        print(f"Secret Word: {sec}")
        print(f"Correct Letters: {correct_letters}")
        print(f"Present Letters: {present_letters}")
        print(f"Missing Letters: {missing_letters}")

    # Get user input from the terminal
    user_input = input("Enter a five-letter word: ")

    # Check if the input is valid (5 characters)
    if len(user_input) != 5:
        print("Please enter a five-letter word.")
        return

    # Call the enter_action function with the user's input
    enter_action(user_input)

# Startup code
if __name__ == "__main__":
    wordle()

            
                


