"""Write a Python program to select an item randomly from a list.
"""
import random

items = ["apple", "banana", "orange", "grape", "mango"]

randomitem = random.choice(items)

print(randomitem)