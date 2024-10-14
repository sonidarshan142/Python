"""Write a Python program to calculate the area of a trapezoid"""

def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezoid: "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is {area}.")

