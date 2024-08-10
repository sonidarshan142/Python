"""Write a Python program to count the occurrences of each word in a
given sentence
"""

a1 = "This is a sentence with some words repeated This is"
a1 = a1.lower()
# Split the sentence into words
words = a1.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
