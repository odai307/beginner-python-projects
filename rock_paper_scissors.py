import random

my_score = 0
cpu_score = 0

while True:
    try:
        score = int(input("Enter the score you want to reach?: "))
        break
    except ValueError:
        "Enter a number"

while my_score < score and cpu_score < score:
    number = random.randint(1, 3)

    select = input("Rock Paper Scissors: ").lower()

    if select == "quit":
        while True:
            quit_game = input("Do you want to quit? Enter Y or N: ").lower()
            if quit_game == "y":
                print("See you later!")
                quit()
            elif quit_game == "n":
                break
            
    if select == "rock":
        if number == 1:
            print("Rock Rock!")
            print(f"{my_score} - {cpu_score}")
        if number == 2:
            print("Paper covers Rock!")
            cpu_score += 1
            print(f"{my_score} - {cpu_score}")
        if number == 3:
            print("Rock breaks scissors!")
            my_score += 1
            print(f"{my_score} - {cpu_score}")
    elif select == "paper":
        if number == 1:
            print("Paper covers Rock!")
            my_score += 1
            print(f"{my_score} - {cpu_score}")
        if number == 2:
            print("Paper Paper!")
            print(f"{my_score} - {cpu_score}")
        if number == 3:
            print("Scissors cuts paper!")
            cpu_score += 1
            print(f"{my_score} - {cpu_score}")
    elif select == "scissors":
        if number == 1:
            print("Rock breaks scissors!")
            cpu_score += 1
            print(f"{my_score} - {cpu_score}")
        if number == 2:
            print("Scissors cuts paper!")
            my_score += 1
            print(f"{my_score} - {cpu_score}")
        if number == 3:
            print("Scissors Scissors!")
            print(f"{my_score} - {cpu_score}")
    

print(f"My Score : {my_score}  Computer Score : {cpu_score}")
if my_score > cpu_score:
    print("Congratulations. You won!")
else:
    print("Sorry. You lost")