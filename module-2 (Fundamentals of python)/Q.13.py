"""Write a Python program to count the number of characters (character 
frequency) in a string"""

a = input("Enter char :")
freq = {}
for i in a:
    if i in freq:
        freq i+= 1
    else:
        freq i=1

print("Count number of char :" + str(freq)) 
