"""Write a Python program to create a dictionary from a string."""

str = "Darshan Manav Meet"
d = {}
for word in str.split():
    d[word] = 1
print(d)