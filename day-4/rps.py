import random
import os
import csv

# Todo - Update leaderboards with current stats when viewed.
# Todo - Add an options menu where u can customize a username for the leaderboard.
# Todo - Ascii-art for hands.
# Todo - Autoplay mode. - Game plays itself with a 1 second sleep or something.
# Todo - update_leaderboard should work with a temporary file.
# Todo - REFACTOR


def main():

    choices = ["ROCK", "PAPER", "SCISSORS"]
    wins = 0
    games = 0

    init_leaderboard()

    print(f"Welcome to {' '.join(choices)}!")
    username = input("What is your username?: ")

    while True:
        clear_console()
        print("ROCK PAPER SCISSORS\n")

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
                options([username, games, wins])

        except ValueError:
            print("Invalid choice.")


def options(stats: list):
    """Options menu"""
    clear_console()

    print("""Options:\n1. Change username\n2. Display leaderboard""")

    user_choice = input(": ")

    if user_choice == "1":
        stats[0] = input("New username: ")
        return stats

    elif user_choice == "2":
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

    leaderboard = []

    # Open file for reading.
    with open("leaderboard.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)

    def sort_wins(i):
        """Sorts the loaderboard basen on wins."""
        return i[2]

    leaderboard.sort(reverse=True, key=sort_wins)
    for i in leaderboard:
        print("\t".join(i))

    # Wait for user input to keep displaying leaderboard?
    input()


def update_leaderboard(stats: list):
    """Updates the leaderboard."""

    read_file = []
    found = 0

    # Read entire leaderboard to read_file.
    with open("leaderboard.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for i in reader:
            if i[0] == stats[0]:
                i = [i[0], int(i[1]) + stats[1], int(i[2]) + stats[2]]
                found = 1
                read_file.append(i)
                continue
            read_file.append(i)
        if found == 0:
            read_file.append(stats)

    # Here we can sort read_file tbh.

    # Write read_file to leaderboard, overwriting entire file.
    with open("leaderboard.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(read_file)


def init_leaderboard():

    fields = ("name", "games", "wins")

    # Create CSV-file if it doesnt exist.
    if not os.path.isfile("leaderboard.csv"):
        with open("leaderboard.csv", "x", newline="") as file:
            writer = csv.DictWriter(file, fields)
            writer.writeheader()


if __name__ == "__main__":
    main()
