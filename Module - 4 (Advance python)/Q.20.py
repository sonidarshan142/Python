"""Write python program that user to enter only odd numbers, else will
raise an exception"""

class EvenNumberError(Exception):
    pass

def get_odd_number():
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise EvenNumberError(f"{number} is an even number!")
        print(f"Great! You entered an odd number: {number}")
    except EvenNumberError as e:
        print(f"Exception: {e}")
    except ValueError:
        print("That's not a valid number! Please enter an integer.")
get_odd_number()
