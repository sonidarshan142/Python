"""Write a Python program to read first n lines of a file."""

f = input("Enter the file name: ")
n = int(input("Enter the number of lines to read: "))
with open(f, "r") as file:
    for i in range(n):
        line = file.readline()
print(line)