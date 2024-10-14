"""Write a Python program to read a random line from a file."""

import random
fd = open("Q.52.txt","r")
lines = fd.readlines()
print(random.choice(lines))
fd.close()