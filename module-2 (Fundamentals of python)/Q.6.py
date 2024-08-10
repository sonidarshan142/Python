# Write python program that swap two number with temp variable and 
# without temp variable.

# Swap two numbers with a temp variable
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp
print("Before swapping:", num1, num2)

# Swap two numbers without a temp variable

num1, num2 = num2, num1
print("After swapping without temp:", num1, num2)





