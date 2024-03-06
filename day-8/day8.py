def paint(height, width, coverage=5):

    area = height * width

    # This returns a float. If it is not evenly divisible by 5, add 1 can.
    cans = area / 5

    if area % 5 != 0:
        cans += 1

    cans = int(cans)

    print(f"You need {cans} cans.")


def prime(num):

    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    paint(6, 4)
    print(prime(2))  # True
    print(prime(5))  # True
    print(prime(10))  # False
    print(prime(15))  # False
    print(prime(13))  # True
    print(prime(1))
