#Write a Python function to insert a string in the middle of a string.

test_str = "Hello world"
mid_str = "the"
print("The original string is :"+str(test_str))
mid_str = input("Enter a middle string: ")

temp = test_str.split()
mid_pos = len(temp)// 2

res = " ".join(temp[:mid_pos]+[mid_str]+temp[mid_pos:])

print(+str(res))

