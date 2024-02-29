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


if __name__ == "__main__":
    odd_or_even()
