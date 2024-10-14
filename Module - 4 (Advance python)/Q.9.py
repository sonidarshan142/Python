"""Write a Python program to count the number of lines in a text file."""

f = "myfile.txt"
with open(f, 'r') as f:
  lines = f.readlines()
print("Number of lines in", f, ":", len(lines))