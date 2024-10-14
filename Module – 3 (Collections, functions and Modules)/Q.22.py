"""Write a Python program to check whether an element exists within a 
tuple."""

t = (10,20,30,40,50,60)

element = 10

if element in t:
    print(f"{element} exists in a tuple")
else:
    print(f"{element}does not exists")