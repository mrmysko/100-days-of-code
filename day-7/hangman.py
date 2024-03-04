import os
import random
import requests
import time

# Todo - Keep the hangman on win-state.
# Todo - Save word_list between runs to minimize network traffic.
# Todo - Hints.


def main():
    clear_console()

    print(
        """ _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """
    )
    time.sleep(1)

    # Init game variables
    word = random_word()
    solved = [0] * len(word)
    max_guesses = 6
    wrong_guess = 0

    while True:

        # Check if game is in an end-state.
        end(word, solved, wrong_guess)

        # Continiously draw the board.
        draw_board(word, solved, wrong_guess)

        # Input a guess
        guess = input("Guess a letter: ").lower().strip()

        # If the guess is not in the word, increment wrong guess.
        if not guess in word:
            wrong_guess += 1

        # Change correct letters to solved status.
        for i, value in enumerate(word):
            if value == guess:
                solved[i] = 1


def random_word():
    """Get a random word."""

    words = []

    # Save URL to word-site.
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    if len(words) == 0:
        # Get the words.
        response = requests.get(word_site)
    words = response.content.splitlines()

    word = random.choice(words)
    word = word.decode("ascii")

    return word


def clear_console():
    """Clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)


def draw_board(word: str, solved: list, wrong_guess: int):
    """Draws the hangman"""

    clear_console()

    # This seems kinda redundant, having a function "draw board" that calls
    # another function to draw the hangman...
    # But how would I draw the hangman on a win-state otherwise if I clear the board
    # on winning?
    print_hangman(wrong_guess)

    for i, value in enumerate(word):
        if solved[i] == 1:
            print(f"{value} ", end="")
        else:
            print("_ ", end="")
    print()


def end(word, solved, wrong_guess):
    """Checks if an end-state is reached."""

    max_guess = 6

    if wrong_guess >= max_guess:
        clear_console()
        print_hangman(wrong_guess)
        print(f'Oh no, he\'s dead! The word was "{word}".')
    elif not 0 in solved:
        clear_console()
        print_hangman(wrong_guess)
        print(f'You won! The word was "{word}".')
    else:
        # If not in end-state, return to main function.
        return

    again = input("Would you like to play again? (Y/N): ").upper()

    if again == "N":
        print("Thank you for playing!")
        exit()
    else:
        main()


def print_hangman(wrong_guess):

    hangman = [
        """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========""",
    ]

    print(hangman[wrong_guess])


if __name__ == "__main__":
    main()
