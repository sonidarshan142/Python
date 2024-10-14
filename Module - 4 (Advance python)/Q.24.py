"""Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the parameter of a circle"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def compute_area(self):
        return 3.14 * (self.radius ** 2)
    
    def compute_parameter(self):
        return 2 * 3.14 * self.radius

circle = Circle(7)
print("Area of the circle:", circle.compute_area())
print("Parameter of the circle:", circle.compute_parameter())
