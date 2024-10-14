"""Write a Python program to read last n lines of a file."""

# Get the file name and number of lines to read
f = input("Enter the file name: ")
n = int(input("Enter the number of lines to read: "))

with open(f, "r") as file:
    lines = file.readlines()

for line in lines[-n:]:
    print(line)