import random
import os
import csv

# Todo - Add file maniulation, make a leaderboard that persists between games.
# Todo - Add an options menu where u can customize a username for the leaderboard.
# Todo - Ascii-art for hands.
# Todo - Repeatedly clear and draw the console, giving it a graphical effect.
# Todo - Autoplay mode. - Game plays itself with a 1 second sleep or something.
# Todo - Split into functions. One function for game logic, one for leaderboard, one for options, one for clearing console etc...
# Todo - update_leaderboard should work with a temporary file.


def main():

    choices = ["ROCK", "PAPER", "SCISSORS"]
    wins = 0
    games = 0

    fields = ("name", "games", "wins")

    # Create CSV-file if it doesnt exist.
    if not os.path.isfile("leaderboard.csv"):
        with open("leaderboard.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fields)
            writer.writeheader()

    print(f"Welcome to {' '.join(choices)}!")
    username = input("What is your username?: ")

    while True:
        print()
        choose = input("Make your choice: ").upper()

        cpu_choice = random.choice(choices)

        try:
            if choices.index(choose) == choices.index(cpu_choice):
                print(f"{choose} tie {cpu_choice}. You tie.")
            elif (choices.index(choose) + 1) % 3 == choices.index(cpu_choice):
                print(f"{cpu_choice} beats {choose}. You lose.")
            else:
                print(f"{choose} beats {cpu_choice}. You win.")
                wins += 1

            games += 1
            print(
                f"{games} games played. You have won {wins} times. {round((wins / games) * 100, 2)}% winrate."
            )
            print()

            # or 'Y' is unnecessary since we only check for a 'N' to stop.
            again = input("Play again (Y/N/O)? ").strip().upper() or "Y"
            if again == "N":
                update_leaderboard([username, games, wins])
                print("Thank you for playing!")
                break
            elif again == "O":
                options()

            # Clear console on new game.
            clear_console()
        except ValueError:
            print("Invalid choice.")

    display_leaderboards()


def options():
    """Options menu"""
    clear_console()

    print("""Options:\n1. Change username\n2. Display leaderboard""")

    user_choice = input(": ")

    if user_choice == "1":
        pass
        # input("New username: ")
    elif user_choice == "2":
        update_leaderboard()
        display_leaderboards()


def clear_console():
    """Clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)


def display_leaderboards():
    """Print out the leaderboard."""
    clear_console()

    # Open file for reading.
    with open("leaderboard.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def update_leaderboard(stats: list):
    """Updates the leaderboard."""

    # Append new name to leaderboard.
    with open("leaderboard.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(stats)


if __name__ == "__main__":
    main()
