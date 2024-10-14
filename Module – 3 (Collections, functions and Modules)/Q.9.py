#  Write a Python function that takes two lists and returns true if they have 
# at least one common member.

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 5]

common_member = False

for i in list1:
    if i in list2:
        common_member = True
    
print(common_member)
