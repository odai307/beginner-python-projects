remaining_attempts = 10
code_answer = "gabriel307"
question = input("Do you want to play the game?: ")
if question == "no":
    print("Thank you. Hope to see you again another time")
    quit()

while question != "yes":
    loop = input("Enter yes to continue or no to quit: ")
    if loop == "no":
        print("Thank you. Home to see you again")
        quit()

    elif loop == "yes":
        break
    
print("Let's start the game")
code = input("Enter password: ")
if code == code_answer:
    print("Congratulatons. You guessed the password right")
    quit()

while code != code_answer:
    remaining_attempts-=1
    print("You have ", str(remaining_attempts), " attempts remaining")
    code =input("Enter password: ")
    
    if remaining_attempts == 1:
        break
    if code == code_answer:
        break

if remaining_attempts >= 1 and code == code_answer:
    print("Congratulatons. You guessed the password right")
else:
    print("Sorry. You are out of tries")




   