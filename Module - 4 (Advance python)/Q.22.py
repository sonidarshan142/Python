"""How to Define a Class in Python? What Is Self? Give An Example Of 
A Python Class

=>class is a userdefined data type.
   which is contain datamember and member functions.
 class is defined usiing class keyword

what is self ?

=> The self parameter in Python is a reference to the current instance of the class. 
   It allows access to the attributes and methods of the class in Python.
It is automatically passed to any method of the class but must be included explicitly when defining the method.
self is not a keyword, but a convention.
"""

class sample:
    #methods inside the class
    def display(self):
        print("Hello welcome to sample class")
    
    def show(self):
        print("class program is here")

obj = sample()
obj.display()
obj.show()

