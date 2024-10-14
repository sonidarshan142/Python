"""Write a Python program to calculate surface volume and area of a 
cylinder"""

import math

def cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def cylinder_surface_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = cylinder_volume(radius, height)
surface_area = cylinder_surface_area(radius, height)

print(f"Volume of the cylinder: {volume:.2f}")
print(f"Surface area of the cylinder: {surface_area:.2f}")
