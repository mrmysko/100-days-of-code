def tip():
    while True:
        try:
            bill = int(input("How big was the bill? $"))
            break
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            tip = int(input("Tip %: "))
            break
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            persons = int(input("How many people should split?: "))
            break
        except ValueError:
            print("Invalid input.")

    total_tip = bill * (tip / 100)
    total_bill = bill + total_tip
    total_per_person = total_bill / persons

    print(
        f"Your tip comes out to {total_tip}, the total bill is {total_bill} and each person should pay {total_per_person}"
    )


def bmi():
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

    print(f"Your BMI is {round(weigth / ((length / 100)**2), 1)}")


def weeks_left():
    # Todo - Implement date library for more accuracy.
    while True:
        try:
            age = int(input("Age (y): "))
            break
        except ValueError:
            print("Expected a number.")

    max_weeks = 52 * 90
    current_weeks = age * 52

    print(f"You have {max_weeks - current_weeks} weeks left until 90.")


if __name__ == "__main__":
    tip()
