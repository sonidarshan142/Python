#Write a Python function to insert a string in the middle of a string.

string = input("Enter a string : ")
insert = input("Enter a middle string : ")

middleindex = len(string) // 2
result = string[:middleindex] + insert + string[middleindex:]

print(result)


