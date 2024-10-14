"""Write a Python program to append text to a file and display the text"""

with open("myfile.txt", "a") as file:
    file.write("This is appended text.\n")

with open("myfile.txt", "r") as file:
    text = file.read()
print(text)
