# accept 5 subjects marks form user and calculate avg.
# make sure each subject marks above 35

sub1 = int(input("Enter marks for Subject 1: "))
if sub1 < 35:
    print("You have failed Subject 1")
else:
    print("You have passed Subject 1")

sub2 = int(input("Enter marks for Subject 2: "))
if sub2 < 35:
    print("You have failed Subject 2")
else:
    print("You have passed Subject 2")

sub3 = int(input("Enter marks for Subject 3: "))
if sub3 < 35:
    print("You have failed Subject 3")
else:
    print("You have passed Subject 3")

sub4 = int(input("Enter marks for Subject 4: "))
if sub4 < 35:
    print("You have failed Subject 4")
else:
    print("You have passed Subject 4")

sub5 = int(input("Enter marks for Subject 5: "))
if sub5 < 35:
    print("You have failed Subject 5")
else:
    print("You have passed Subject 5")

total = sub1 + sub2 + sub3 + sub4 + sub5 
avg = total / 5

print(f"Total marks: {total}")
print(f"Average marks: {avg}")
