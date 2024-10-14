"""What is Instantiation in terms of OOP terminology?"""

"""Instantiation is the process of creating an object (or instance) from a class. 
When you define a class in OOP, you're essentially creating a blueprint for objects, 
but the actual object itself does not exist until you instantiate it."""


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Car: {self.make} {self.model}"

my_car = Car("Toyota", "fortuner")

print(my_car.display_info())
