"""Write a Python program to find the repeated items of a tuple."""

t=(1,2,3,4,1,4,5,7,5,8)  
for i in t:
    if t.count(i) > 1:
        print(i)