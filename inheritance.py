class Furniture:
    def __init__(self):
        self._typeOfFurniture = "Teakwood"

class Chair(Furniture):
    __numberOfLegs = 4
    def changeTypeOfFurniture(self, newType):
        self._typeOfFurniture = newType
    def displayChairDescription(self):
        print("This chair is made of {} and has {} legs".format(self._typeOfFurniture, self.__numberOfLegs))

chair = Chair()
print("Would you like to change the type of wood from Teakwood? Y/N")
userChoice = input()
if userChoice == "Y":
    print("What would you like to change the type of wood to?")
    newType = input()
    chair.changeTypeOfFurniture(newType)
chair.displayChairDescription()
