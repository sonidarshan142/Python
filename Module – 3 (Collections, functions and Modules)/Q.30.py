"""Write a Python program to convert a list of tuples into a dictionary."""

tuples = [("Darshan", 1), ("Pratham", 2), ("Dhaval", 3)]

d = {}

for t in tuples:
    d[t[0]] = t[1]

print(d)