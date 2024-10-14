"""Write a Python program to read a file line by line and store it into a list"""

f = input("Enter the file name: ")

with open(f, "r") as file:
    list = []

    for line in file:
        list.append(line)

print(list)