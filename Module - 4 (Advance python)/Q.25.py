"""Explain Inheritance in Python with an example? What is init? Or What 
Is A Constructor In Python?"""

"""inheritance : one class derived properties of another class its called inheritance

                which is provide reusablity and which can reduce our code.

                using of inheritance we can save our time."""

class parent:
    def display1(self):
        print("parent class is here")

class child(parent):
    def display2(self):
        print("child class is here")

obj = child()
obj.display1()
obj.display2()

"""what is init ?
=> In Python, the __init__ method is called a constructor. It’s a special method that gets 
called when an object is instantiated (created) from a class. The purpose of __init__ is
 to initialize the object's attributes (properties).
"""