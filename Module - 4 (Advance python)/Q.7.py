"""Write a Python program to read a file line by line store it into a variable."""

f = input("Enter the file name: ")
with open(f, "r") as file:
    content = file.readlines()

content = "".join(content)
print(content)