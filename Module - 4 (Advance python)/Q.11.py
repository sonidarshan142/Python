"""Write a Python program to write a list to a file."""

l = ["apple", "banana", "cherry", "date"]

with open("list.txt", "w") as file:
    for item in l:
        file.write(item + "\n")