"""Write a Python script to concatenate following dictionaries to create a
new one."""

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

newdict = dict1.copy()
newdict.update(dict2)

print("Concatenated dictionary:", newdict)