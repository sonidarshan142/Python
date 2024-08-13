"""Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string."""

a1 = input("Enter a string: ")
notindex = a1.find('not')
poorindex = a1.find('poor')

if notindex != -1 and poorindex != -1 and notindex < poorindex:
    string = string[:notindex] + 'good' + string[poorindex + 4:]
else:
    string = string

print(a1)
