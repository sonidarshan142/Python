"""Write a Python function that checks whether a passed string is 
palindrome or not"""

def is_palindrome(s):
  s = s.lower().replace(' ', '')
  return s == s[::-1]

s = input("Enter a string :")
print(is_palindrome(s))
