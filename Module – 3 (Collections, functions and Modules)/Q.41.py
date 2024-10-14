"""Write a Python program to combine two dictionary adding values for 
common keys."""

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'a': 30, 'b': 20, 'd': 40}

combined_dict = {}

for key in d1:
    combined_dict[key]=d1[key]

for key in d2:
    if key in combined_dict:
        combined_dict[key]+=d2[key]
    else:
        combined_dict[key]=d2[key]

print(combined_dict)
