"""
Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3 If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged
"""
string = input("Enter a string: ")
if len(string) >=3:
    if string.endswith('ing'):
        string += 'ly'
    else:
        string += 'ing'
print(string)
