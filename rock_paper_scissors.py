import random

my_score = 0
cpu_score = 0
select = input("Rock Paper Scissors: ").lower()

while select != "rock" and select != "paper" and select != "scissors":
    print("Invalid. Try again!")
    select = input("Rock Paper Scissors: ")    
    if select == "rock" or select == "paper" or select == "scissors":
        break

while my_score < 10 and cpu_score < 10:
    number = random.randint(1, 3)    
    if select == "rock":
        if number == 1:
            print("Rock Rock. Draw game!")
            print(f"my score: {my_score} cpu score: {cpu_score}")
        if number == 2:
            print("Paper covers Rock. You lost!")
            cpu_score += 1
            print(f"my score: {my_score} cpu score: {cpu_score}")
        if number == 3:
            print("Rock breaks scissors. You won!")
            my_score += 1
            print(f"my score: {my_score} cpu score: {cpu_score}")
    elif select == "paper":
        if number == 1:
            print("Paper covers Rock. You won!")
            my_score += 1
            print(f"my score: {my_score} cpu score: {cpu_score}")
        if number == 2:
            print("Paper Paper. Draw game!")
            print(f"my score: {my_score} cpu score: {cpu_score}")
        if number == 3:
            print("Scissors cuts paper. You lost!")
            cpu_score += 1
            print(f"my score: {my_score} cpu score: {cpu_score}")
    elif select == "scissors":
        if number == 1:
            print("Rock breaks scissors. You lost!")
            cpu_score += 1
            print(f"my score: {my_score} cpu score: {cpu_score}")
        if number == 2:
            print("Scissors cuts paper. You won!")
            my_score += 1
            print(f"my score: {my_score} cpu score: {cpu_score}")
        if number == 3:
            print("Scissors Scissors. Draw game!")
            print(f"my score: {my_score} cpu score: {cpu_score}")
    select = input("Rock Paper Scissors: ")

print(f"My Score : {my_score}  Computer Score : {cpu_score}")
if my_score > cpu_score:
    print("Congratulations. You won!")
else:
    print("Sorry. You lost")

