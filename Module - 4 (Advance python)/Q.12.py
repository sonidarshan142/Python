"""Write a Python program to copy the contents of a file to another file."""

file = input("Enter the name of the source file: ")
another_file = input("Enter the name of the destination file: ")

with open(file, "r") as source, open(another_file, "w") as copy:
    for line in source:
        copy.write(line)

print("File copied successfully!")