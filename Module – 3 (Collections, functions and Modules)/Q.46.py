"""Write a Python program to combine values in python list of dictionaries."""

d = [
    {'name': 'Darshan', 'age': 20, 'city': 'Viramgam'},
    {'name': 'Manav', 'age': 18, 'city': 'Ahmedabad'},
    {'name': 'Meet', 'age': 24, 'city': 'Viramgam'}
]

combined_data = {}

for value in d:
    for key, value in value.items():
        combined_data[key] = combined_data.get(key, []) + [value]

print(combined_data)