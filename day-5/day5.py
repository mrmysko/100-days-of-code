def avg_height():

    heights = [120, 145, 78, 156, 177, 90, 100]
    total_height = 0

    for i in heights:
        total_height += i

    print(
        f"The average height of {len(heights)} students was {round(total_height / len(heights), 2)}"
    )


def highscore():

    scores = [45, 67, 34, 32, 56, 84, 23, 45, 56]
    highscore = 0

    for i in scores:
        if i > highscore:
            highscore = i

    print(f"The highest score is: {highscore}")


def even_add(n):

    total = 0

    for i in range(2, n + 1, 2):
        total += i

    print(f"Total: {total}")


def fizzbuzz(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(30)
