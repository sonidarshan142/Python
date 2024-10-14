"""Write a Python program to calculate the area of a parallelogram"""

def parallelogram_area(base, height):
    return base * height
base_length = float(input("Enter the base length of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = parallelogram_area(base_length, height)

print(f"The area of the parallelogram is: {area:.2f}")
