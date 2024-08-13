"""Write a Python program to count the number of characters (character 
frequency) in a string"""

a = input("Enter char :")
count = {}

for char in a:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1 


for char, count in count.items():
    print(f"{char}: {count}")
