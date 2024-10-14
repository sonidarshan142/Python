"""
Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.
"""

strings = ['Darshan','Pratham','Kaushal','121','aba']

count = 0

for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of strings with length 2 or more and same first/last characters:", count)
