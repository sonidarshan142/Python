# accept temp value from user.
# air water ice

temp = int(input("Enter temp value :"))

if temp <0:
    print("ice")
elif temp >=0 and temp <=100:
    print("water")
else:
    print("air")
