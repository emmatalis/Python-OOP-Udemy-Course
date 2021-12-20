class PreciousStone:
    numberOfPreciousStones = 0
    preciousStoneCollection = []
    def __init__(self, name):
        self.name = name
        # increment the number of precious precious stones
        PreciousStone.numberOfPreciousStones += 1
        # append precious stone to the list if total num of stones was < 5
        if PreciousStone.numberOfPreciousStones <= 5:
            PreciousStone.preciousStoneCollection.append(self)
        else:
            # if more than 5 existed already, delete first & then append
            del PreciousStone.preciousStoneCollection[0]
            PreciousStone.preciousStoneCollection.append(self)

    @staticmethod
    def displayPreciousStones():
        for preciousStone in PreciousStone.preciousStoneCollection:
            print(preciousStone.name, end = " ")
        print()


preciousStoneOne  = PreciousStone("Ruby")
preciousStoneTwo  = PreciousStone("Emerald")
preciousStoneThree  = PreciousStone("Sapphire")
preciousStoneFour  = PreciousStone("Diamond")
preciousStoneFive  = PreciousStone("Amber")
preciousStoneFive.displayPreciousStones()
preciousStoneSix = PreciousStone("Onyx")
# Print all the stones after deleting the first stone
preciousStoneSix.displayPreciousStones()
