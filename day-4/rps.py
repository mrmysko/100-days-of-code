import random

# Todo - Add file maniulation, make a leaderboard that persists between games.
# Todo - Add an options menu where u can customize a username for the leaderboard.
# Todo - Ascii-art for hands.
# Todo - Repeatedly clear and draw the console, giving it a graphical effect.


def main():

    choices = ["ROCK", "PAPER", "SCISSORS"]
    wins = 0
    games = 0

    print(f"Welcome to {' '.join(choices)}!")

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
            again = input("Play again (Y/N)? ").strip().upper() or "Y"
            if again == "N":
                print("Thank you for playing!")
                break
        except ValueError:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
