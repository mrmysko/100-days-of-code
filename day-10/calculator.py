import os


def main():
    while True:
        clear_console()
        draw_board()

        num_one = int(input("What's the first number?: "))
        print("+\n-\n*\n/")
        operator = input("Pick and operator: ")
        num_two = int(input("What's the second number?: "))

        print(num_one, operator, num_two, "= ", end="")

        match operator:
            case "+":
                print(num_one + num_two)
            case "-":
                print(num_one - num_two)
            case "*":
                print(num_one * num_two)
            case "/":
                print(num_one / num_two)
            case _:
                print("Error.")

        input()


def draw_board():

    numbers = 0
    calc = f""" _____________________
|  _________________  |
| |              {numbers}. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

    print(calc)


def clear_console():
    """Clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)


if __name__ == "__main__":
    main()
