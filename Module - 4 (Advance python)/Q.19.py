"""How Do You Handle Exceptions With Try/Except/Finally In Python? 
Explain with coding snippets."""

"""1. try block: Contains code that might raise an exception.
2. except block: Handles the exception if one occurs in the try block.
3. finally block: Contains code that will always execute, regardless of whether an exception occurred or not.
"""

try:
    x = 10 / 0 
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
finally:
    print("This program runs.")
