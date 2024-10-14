"""Write a Python program to convert degree to radian"""

import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = float(input("Enter a number : "))
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians} radians.")
