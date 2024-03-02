import random
import os


def main():

    chars = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz"
    special_chars = "#%&$£@"
    digit_chars = "123456789"

    print("Welcome to password generator.")

    password = []

    while True:
        try:
            pass_num = int(input("How many passwords do you want to generate?: ") or 1)

            total_len = int(input("Password length: "))

            spec_len = int(input("How many special chars?: "))

            digit_len = int(input("How many numbers?: "))

            break
        except ValueError:
            print("Only numbers allowed.")

    os.system("clear")
    print(f"Generateing {pass_num} passwords:\n")

    for i in range(pass_num):
        for i in range(spec_len):
            password.append(random.choice(special_chars))

        for i in range(digit_len):
            password.append(random.choice(digit_chars))

        while len(password) < total_len:
            password.append(random.choice(chars))
            random.shuffle(password)
            password_str = "".join(password)

        print(password_str)


if __name__ == "__main__":
    main()
