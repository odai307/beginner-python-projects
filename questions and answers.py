
score = 0

wanna_answer = "Do you want to answer the questions? "
if wanna_answer == "no":
    quit()
while wanna_answer != "yes":
    loop = input("Enter yes or no to continue ")
    if loop == "no":
        quit()
    elif loop == "yes":
        break

first_question = input("What is the Capital City of Ghana. ")
if first_question == "accra":
    score += 2
else:
    score -=1

second_question = input("What is the full meaning of C.P.U ")
if second_question == "central processing unit":
    score += 2
else:
    score -= 1

third_question = input("Which sense organ is used for breathing ")
if third_question == "nose":
    score += 2
else:
    score -= 1

fourth_question = input("What is the biggest country in the world ")
if fourth_question == "russia":
    score += 2
else:
    score -= 1

fifth_question = input("What is the official language of Ghana ")
if fifth_question == "english":
    score += 2
else:
    score -= 1

print("Your score was" + str(score/10*100) + "%")

