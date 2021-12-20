# Abstract Base Class (ABC)
# does not have a definition of its own, it only has abstract methods which then
# MUST be defined in the derived class of this ABC
# if the methods of the ABC are not defined in all derived classes,
# Python throws an error:
# "Can't instantiate abstract class Square with abstract method area"
# you cannot instantiate object from an abstract class
# ABCs are designed to force implementation within derived classes

from abc import ABCMeta, abstractmethod # import from ABC module in python

class Shape(metaclass = ABCMeta): # making it an abstract base class
    @abstractmethod # decorate
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of square: ", self.side * self.side)

class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print("Area of rectangle: ", self.width * self.length)

square = Square()
rectangle = Rectangle()

square.area()
rectangle.area()
shape = Shape()
