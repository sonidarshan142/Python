"""Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string."""

a1 = input("Enter a string: ")
not_index = a1.find('not')
poor_index = a1.find('poor')

if not_index !=1 and poor_index !=-1 and not_index>poor_index:
    a1=a1[:poor_index]+ 'Good'+ a1[:poor_index +4:]

print(a1)