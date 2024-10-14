"""Write a Python program to check multiple keys exists in a dictionary"""

d = {
  'name': 'Darshan',
  'age': 21,
  'city': 'Ahmedabad'
}
print(d.keys() >= {'age', 'name'})
print(d.keys() >= {'name', 'Darshan'})
print(d.keys() >= {'city', 'Ahmedabad'})