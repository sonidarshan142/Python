"""Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary."""

import itertools
my_letters = {"A": ["a", "b"], "B": ["c", "d"], "C": ["e", "f"]}

keys = list(my_letters.keys())
letters = [my_letters[key] for key in keys]
combos = ["".join(combo) for combo in itertools.product(*letters)]

print(combos)