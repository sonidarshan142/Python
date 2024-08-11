"""
Accept name and password from user
check validation

make sure name must be 4 or more characters contain
make sure name contains only char otherwise return specific error message
password must be 8 or 10 char required
make sure password must contain char and numbers
"""

name = input("Enter your name: ")
len_name = len(name)
char = (name.isalpha())
if len_name<4:
    print("please enter 4 char")
elif not name.isalpha():
    print("use only alphabates")
else:
    print("name: ",name)

password = input("Enter your password")
if len(password)<8:
    print("Enter atleast 8 char in password")
elif password != password.isalnum():
    print("You have use alphabates and numbers")
else:
    print("password ",password)