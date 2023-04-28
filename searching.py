import random

while True:
    try:
        number_range = int((input("Enter A number range from 0: ")))
        break
    except ValueError:
        print("Enter a valid number")

random_number = random.randint(0, int(number_range))

while True:
    try:
        number = input(f"Enter a Number between 0 and {number_range}: ")
    except ValueError:
        print("Enter a valid number")

    if int(number) == random_number:
        print("Number found")
        quit()
    elif int(number) > random_number:
        print("Too large")
    else:
        print("Too small")
