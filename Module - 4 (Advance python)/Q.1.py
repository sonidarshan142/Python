"""What is File function in python? What is keywords to create and write 
file.

ans : In Python, working with files involves using the built-in open() function 
      to interact with files on your system. 
      This function allows you to read from, write to, and create files.

"x" (Create): This mode creates a new file if it doesnt already exist. 
If a file with the same name exists, it will return an error.

"a" (Append): Use this mode to create a file if it doesnt exist. 
If the specified file already exists, it will append content to the end of the file.

"w" (Write): Similar to "a", this mode creates a file if it doesnt exist.
 However, if the file exists, it will overwrite its entire content.
"""

# Create an empty text file called "myfile.txt"
f = open("myfile.txt", "x")