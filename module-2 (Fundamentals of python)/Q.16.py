"""Write a Python program to count the occurrences of each word in a
given sentence
"""
a1 = input("Enter char : ")
a1 = a1.lower()
# Split the sentence into words
words = a1.split()
wordcount = {}

for word in words:
    wordcount[word] = wordcount.get(word, 0) + 1

print(wordcount)
