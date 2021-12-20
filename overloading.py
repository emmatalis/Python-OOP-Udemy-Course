class Square:
    def __init__(self, side):
        self.side = side

    def __add__(squareOne, squareTwo): # special method "add"
        # which overloads the "+" operatore
        # just need to know the special method/name of the operator
        return((4 * squareOne.side) + (4 * squareTwo.side))

square1 = Square(5) # 5 * 4 = 20
square2 = Square(10) # 10 * 4 = 40
print("Sum of the sides of both squares = ", square1 + square2) # 20 + 40 = 60
