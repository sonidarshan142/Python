"""
• Can one block of except statements handle multiple exception?
syntax :

try:
except ExceptionType1:
except ExceptionType2:
except (ExceptionType3, ExceptionType4):
except Exception:
"""

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both numbers must be numeric.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = divide_numbers(num1, num2)
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers.")