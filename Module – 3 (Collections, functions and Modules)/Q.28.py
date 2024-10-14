"""Write a Python program to remove an empty tuple(s) from a list of tuples."""

l1 = [(10,20,30), (), (40,50,60), (), (70,80,90)]

t = [tuple for tuple in l1 if tuple]
print(t)