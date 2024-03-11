import os


def main():
    clear_console()

    bids = {}

    while True:
        name = input("What is your name?: ")
        bid = input("What's your bid?: $")

        bids[name] = bid

        cont = input("Are there any other bidders? ").lower()
        if cont == "no":
            highest(bids)
            break


def highest(bids: dict):
    name = max(bids, key=bids.get)
    print(f"The highest bidder is {name} with ${bids[name]}")


def clear_console():
    """Clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)


if __name__ == "__main__":
    main()
