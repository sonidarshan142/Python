"""
 Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = False

if num1 == num2:
    result = True
elif abs(num1 - num2) == 5:
    result = True
elif abs(num1 + num2) == 5:
    result = True
else:
    print(result)


