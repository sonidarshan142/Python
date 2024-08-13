"""
Write a Python function that takes a list of words and returns the length 
of the longest one.
"""

maxlength = 0
words = input("Enter a string: ").split()

for word in words:
    maxlength = max(maxlength, len(word))

print(maxlength)
