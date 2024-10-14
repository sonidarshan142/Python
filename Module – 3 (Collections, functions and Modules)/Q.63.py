"""Write a Python program to returns sum of all divisors of a number"""

def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

number = int(input("Enter a number: "))
result = sum_of_divisors(number)
print(f"The sum of all divisors of {number} is: {result}")
