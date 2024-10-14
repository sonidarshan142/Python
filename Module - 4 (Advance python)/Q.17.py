"""When is the finally block executed?"""

try:
    file = open("myfile.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    if file:
        file.close()
        print("File closed.")