"""When will the else part of try-except-else be executed?
Ans : The else part of a try-except-else block is executed only if no exception 
is raised within the try block.In other words, if the code in the try block 
 runs without encountering any errors, the else block will be executed.
"""

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Division was successful.")