"""Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers."""

def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

numbers_input = input("Enter decimal numbers : ")
numbers = list(map(float, numbers_input.split()))
max_num, min_num = find_max_min(numbers)

print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")
