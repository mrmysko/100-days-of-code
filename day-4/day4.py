import random


def heads_or_tails():
    choices = ["H", "T"]
    games = 0
    win = 0

    while True:
        select = input("Heads or tails (H/T)?: ").upper()

        if select == random.choice(choices):
            print(f"{select}. You win!")
            win += 1
        else:
            print("You lost.")

        games += 1

        print(f"You have won {win} times. {(win / games) * 100}% winrate.")


def bankers_roulette(names):
    # Not allowed to use random.choice

    names = names.split(", ")

    index = random.randint(0, len(names) - 1)

    print(f"{names[index]} is going to pay the meal toady!")


def trasure_map():
    cols = "ABC"
    line1 = [" ", " ", " "]
    line2 = [" ", " ", " "]
    line3 = [" ", " ", " "]

    map = [line1, line2, line3]
    row, col = input("Where do you want to hide your map? ").split()

    row = int(row) - 1
    col = cols.find(col)

    print("Hiding your treasure! X marks the spot.")

    map[row][col] = "X"

    print(f"{line1}\n{line2}\n{line3}")


if __name__ == "__main__":
    trasure_map()
