class Employee:
    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.NumberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        # overrides (redefines) base class method of same name
        self.NumberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        # super() transfers control to base class
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end = " ")
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = " ")
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee after reset: ", end = " ")
trainee.displayNumberOfWorkingHours()
