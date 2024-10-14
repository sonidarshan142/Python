"""Write a Python program to find the highest 3 values in a dictionary"""

d = {
    'a' : 5,
    'b' : 10,
    'c' : 15,
    'd' : 30,
    'e' : 60,
    'f' : 80
}
highest_value = sorted(d.values(), reverse=True)[:3]
print("Highest 3 values:", highest_value)