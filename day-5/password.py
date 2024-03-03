import random
import os


def main():

    chars = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz"
    special_chars = "#%&$£@"
    digit_chars = "123456789"

    print("Welcome to password generator.")

    while True:
        try:
            pass_num = int(input("How many passwords do you want to generate?: ") or 1)

            total_len = int(input("Password length: "))

            spec_len = int(input("How many special chars?: "))

            digit_len = int(input("How many numbers?: "))

            break
        except ValueError:
            print("Only numbers allowed.")

    clear_console()
    print(f"Generating {pass_num} passwords:\n")

    for i in range(pass_num):
        password = []
        for i in range(spec_len):
            password.append(random.choice(special_chars))

        for i in range(digit_len):
            password.append(random.choice(digit_chars))

        while len(password) != total_len:
            password.append(random.choice(chars))

        random.shuffle(password)
        password_str = "".join(password)

        print(password_str)


def clear_console():
    """Clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)


if __name__ == "__main__":
    main()
