import random

#Asking the user a range of values he wants to select his number from
while True:
    try:
        number_range = int((input("Enter A number range from 2: ")))
        if number_range <= 1:
            print("Enter a Number Greater than 1")
            continue
        break
    except ValueError:
        print("Enter a valid number")

random_number = random.randint(1, int(number_range))

#Determining the attempts remaining depending on the range of numbers the user selected
attempts_remaining = 0
to_range = 1
while to_range < number_range:
    to_range *= 2
    attempts_remaining += 1

while True:
    if attempts_remaining <= 0:
        print("Attempts exhausted! Game Over")
        print(f"The Random number was {random_number}")
        quit()
        
    try:
        number = int(input(f"Guess the Random Number between 1 and {number_range}: "))
    
    except ValueError:
        print("Enter a valid number")

    else:
        if int(number) == random_number:
            print("Number found")
            print("You won!")
            quit()

        elif int(number) > random_number:
            attempts_remaining -= 1
            if attempts_remaining > 0:
                print("Too large")
                print(f"Attempts remaining: {attempts_remaining}")
        else:
            attempts_remaining -= 1
            if attempts_remaining > 0:
                print("Too small")
                print(f"Attempts remaining: {attempts_remaining}")