"""Write a Python program to unzip a list of tuples into individual lists."""

tuples = [(1, 2), (3, 4), (5, 6)]

l1 = []
l2 = []

for t in tuples:
    l1.append(t[0])
    l2.append(t[1])

print(l1)
print(l2)