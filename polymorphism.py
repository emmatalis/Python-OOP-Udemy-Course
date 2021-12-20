class Square:
    def __init__(self, side):
        self.side = side

    def __pow__(squareOne, squareTwo):
        return(squareOne.side ** squareTwo.side)

square1 = Square(2)
square2 = Square(4)
print("Side of square1 to the power of side of square2 = ", square1 ** square2)
