# Similar to a library management system, write a program to provide layers of abstraction for a car rental system
# Hatchback, Sedan, SUV should be type of cars that are being provided for rent
# Cost per day:
# Hatchback - $30
# Sedan - $50
# SUV - $100
# Give a prompt to the customer asking the type of car & num of days to borrow
# &  provide the fare details to the user

# class = rental company
# layers of abstraction => display cars for rent, give fare details

class RentalCompany:
    def __init__(self):
        # dictionary
        self.carFares = {"Hatchback": 30, "Sedan": 50, "SUV": 100}

    def displayFares(self):
        print()
        print("Cost per day: ")
        print("Hatchback: $", self.carFares["Hatchback"])
        print("Sedan: $", self.carFares["Sedan"])
        print("SUV: $", self.carFares["SUV"])
        print()

    def calculateFares(self, carType, days):
        return self.carFares[carType] * days


rentalCompany = RentalCompany()

while True:
    print("Menu: ")
    print("Enter 1 to display fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")

    userChoice = int(input())

    if userChoice == 1:
        rentalCompany.displayFares()
    elif userChoice == 2:
        print("Please enter the type of car you would like to borrow: ")
        carType = input()
        print("Please enter the number of days you would like to borrow the", carType)
        days = int(input())
        fare = rentalCompany.calculateFares(carType, days)
        print("The cost to rent a", carType, "for", days, "days is: $", fare)
        print("Thank you!")
        print()
    elif userChoice == 3:
        quit()
    else:
        print("Please enter a number 1-4")
