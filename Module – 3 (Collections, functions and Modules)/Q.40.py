"""Write a Python program to map two lists into a dictionary"""

keys = ['a', 'b', 'c']
values = [1, 2, 3]

d = dict(zip(keys, values))

print(d)