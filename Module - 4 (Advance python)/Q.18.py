"""What happens when „1‟== 1 is executed?"""

"""In Python, when "1" == 1 is executed, the result will be False.

This is because == is the equality operator, and it checks whether the two values on either side are equal.

"1" is a string (text), while 1 is an integer (number).
Python does not implicitly convert the string "1" to the integer 1 for comparison.
Since a string and an integer are of different data types, they are not considered equal.
Therefore, "1" == 1 evaluates to False."""

result = "1" == 1
print(result)
