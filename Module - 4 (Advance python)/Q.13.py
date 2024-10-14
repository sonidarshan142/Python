"""Explain Exception handling? What is an Error in Python?"""

"""exeception :- its disturb the normal flow of the program its calls exeception.

using of try and except block we can handle exeception.

exeception handling means to handle such kind of exeception in program.
"""

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Finally block executed.")