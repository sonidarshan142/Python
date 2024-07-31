"""
accept 5 numbers from user and check entered number is even or odd.
calculate total even numbers addition and calculate total odd numbers addition.
"""
e_sum = 0
o_sum = 0
for row in range(1,6):
    num = int(input("Enter a number :"))
    if num%2==0:
        e_sum += num
    else:
        o_sum += num

print("even sum =",e_sum)
print("even sum =",o_sum)