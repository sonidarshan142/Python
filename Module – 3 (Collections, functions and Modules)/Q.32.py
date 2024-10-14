"""Write a Python script to sort (ascending and descending) a dictionary by 
value."""

my_dict = {'apple': 10, 'banana': 2, 'cherry': 15, 'mango': 5}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("ascending order:")
print(ascending)

print("\ndescending order:")
print(descending)
