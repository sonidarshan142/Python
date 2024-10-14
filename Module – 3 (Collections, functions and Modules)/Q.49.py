"""Write a Python function to check whether a number is in a given range."""

def range(number, start, end):
  return start <= number <= end
number = 5
start = 1
end = 10
print(range(number, start, end))