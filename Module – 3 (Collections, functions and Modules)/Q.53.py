"""How can you pick a random item from a list or tuple?"""

import random

list = [1, 2, 3, 4, 5]
tuple = ("apple", "banana", "mango", "lichi")

random_list = random.choice(list)
random_tuple = random.choice(tuple)

print(random_list)
print(random_tuple) 