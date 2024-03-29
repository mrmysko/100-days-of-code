import calendar


def odd_or_even():
    while True:
        try:
            number = int(input("Number: "))
            break
        except ValueError:
            print("Number required.")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def bmi2():
    while True:
        try:
            length = int(input("Length (cm): "))
            break
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            weigth = int(input("Weigth (kg): "))
            break
        except ValueError:
            print("Invalid input.")

    bmi = round(weigth / ((length / 100) ** 2), 1)

    print(f"Your BMI is {bmi}")

    match weigth:
        case _ if bmi <= 18.5:
            print("You are underweigth.")
        case _ if 25 > bmi >= 18.5:
            print("You are normal.")
        case _ if 30 > bmi >= 25:
            print("You are overweigth.")
        case _ if bmi >= 30:
            print("You are obese.")


def leap_year():
    while True:
        try:
            year = int(input("Enter a year: "))
            break
        except ValueError:
            print("Require digits.")

    if calendar.isleap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is NOT a leap year.")


def pizza():
    total = 0
    pizzaz = 0

    while True:
        pizza_price = 0

        size = input("Size (S, M, L)? ").upper()
        if size == "S":
            pizza_price += 15
        elif size == "M":
            pizza_price += 20
        elif size == "L":
            pizza_price += 25

        pepper = input("Extra pepperoni (Y/N)? ").upper()
        if pepper == "Y":
            match size:
                case "S":
                    pizza_price += 2
                case _:
                    pizza_price += 3

        cheese = input("Extra cheese (Y/N)? ").upper()
        if cheese == "Y":
            pizza_price += 1

        pizzaz += 1
        total += pizza_price
        more = input(f"Pizza price: ${pizza_price}, order another (Y/N)? ").upper()

        if more == "N":
            break

    print(f"You ordered {pizzaz} pizzaz, total comes out to ${total}.")


def love():
    # This does not handle names with more than one first and surname.

    first_name1, last_name1 = input("What is your name? ").split()
    first_name2, last_name2 = input("What is their name? ").split()

    first_names = first_name1 + first_name2
    last_names = last_name1 + last_name2

    score1 = 0
    score2 = 0

    for i in first_names:
        if i.upper() in "TRUE":
            score1 += 1

    for i in last_names:
        if i.upper() in "LOVE":
            score2 += 1

    score_str = str(score1) + str(score2)
    if 90 < int(score_str) < 10:
        print(f"Your score is {score_str}. You go together like coke and mentos.")
    elif 50 >= int(score_str) >= 40:
        print(f"Your score is {score_str}. You are alright together.")
    else:
        print(f"Your score is {score_str}.")


if __name__ == "__main__":
    love()
