"""Write a Python function that takes a list and returns a new list with unique 
elements of the first list."""


l1 = [10,20,30,10,40,45,40]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)