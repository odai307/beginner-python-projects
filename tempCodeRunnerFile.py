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