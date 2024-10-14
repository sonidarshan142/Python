"""How Do You Traverse Through A Dictionary Object In Python?"""

# create a python dictionary 
d = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
print('List Of given capitals:\n')

for capital in d.values():
    print(capital)
