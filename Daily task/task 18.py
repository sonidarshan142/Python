# accept 4 numbers from user and check enterd number is positive or negative using while loop

i = 1
while i<=4:
    num = int(input("Enter value :"))
    print(num)

    if num>=0:
        print("positive")
    else:
        print("negative")
    i+=1

