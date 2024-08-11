import random

computer = random.randint(1, 100)
status = 5 

while status > 0:
    user = int(input("Enter your number: "))

    if user > computer:
        print("HINT: Guess a lower number")
    elif user < computer:
        print("HINT: Guess a higher number")
    else:
        print(" You guessed it right!")
        break 

    status -= 1 
    if status == 0:
        print(f"The correct number was: {computer}")
