"""
Write a Python function that takes a list of words and returns the length 
of the longest one.
"""

max_length = 0
words = input("Enter a string: ").split()

for word in words:
    max_length = max(max_length, len(word))

print(max_length)
