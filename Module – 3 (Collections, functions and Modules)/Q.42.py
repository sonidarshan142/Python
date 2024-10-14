"""Write a Python program to print all unique values in a dictionary."""

d = {
    'a': 1,
    'b': 2, 
    'c': 1, 
    'd': 3}

print({value for value in d.values()})
