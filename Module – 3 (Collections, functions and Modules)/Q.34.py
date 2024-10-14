"""Write a Python script to check if a given key already exists in a 
dictionary."""

d = {'sub':'python',
    'framework':'django',
    'marks':85,
    'skills':['communication','technical','presentation']}

key_check = 'framework'

if key_check in d:
    print("key exists")
else:
    print("key does not exists")