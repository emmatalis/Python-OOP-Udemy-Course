# naming conventions
# Public => memberName
# Protected (only accessible by this class & derived classes) => _memberName
# ^ this is not syntactically forced, it's just a naming convention that good
# programmers will follow
# Private (only accessible by this class) => __memberName
# ^ this is syntactically forced but only coincidentally, you can get around it

class Car:
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacture = 2017 # accessible anywhere by _Car__yearOfManufacture

class Bmw(Car):
    def __init__(self):
            print("Protected attribute color:", self._color)

car = Car()
print("Public attribute numberOfWheels:", car.numberOfWheels)
bmw = Bmw()

# this works (the work-around):
print("Private attribute yearOfManufacture:", car._Car__yearOfManufacture)
# this doesn't work (meaning the attribute is actually private):
print("Private attribute yearOfManufacture:", car.__yearOfManufacture)
