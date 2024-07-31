e_count= 0
o_count = 0
for row in range(1,6):
    num = int(input("Enter a number :"))
    if num%2==0:
        e_count +=1
    else:
        o_count +=1

print("total even =",e_count)
print("total odd =",o_count)