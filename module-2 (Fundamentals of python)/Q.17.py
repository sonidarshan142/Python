"""
Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
"""

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# swapping
newstr1 = str2[:2] + str1[2:]
newstr2 = str1[:2] + str2[2:]

#combine
result = newstr1 + " " + newstr2
print(result)

