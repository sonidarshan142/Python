"""Write a Python program to replace last value of tuples in a list."""

list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_list = [(tuple[:-1] + (10,)) for tuple in list]
print(new_list)