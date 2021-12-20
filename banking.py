# Give a prompt to the user asking if they wish to create a new Savings Account
# or access an existing one
# If the user would like to create a new account, accept their name and
# initial deposit, and create a 5 digit random number as the account number
# If they are accessing an existing account, accept their name & account num to
# validate the user, and then give them options to withdraw, deposit, or display
# their available balance

from random import randint

class SavingsBank:
    activeSavingsAccounts = {}

    def createNewAccountNumber(self):
        while True:
            newAccountNumber = str(randint(10000, 99999))
            # check if this account number is already in use
            if newAccountNumber not in self.activeSavingsAccounts:
                return(newAccountNumber)
                break

    def createNewSavingsAccount(self, accountNumber, name, initialDeposit):
        self.activeSavingsAccounts[accountNumber] = {"name": name, "balance": initialDeposit}

    def displayAvailableBalance(self, accountNumber):
        print("Your available balance is ${}".format(self.activeSavingsAccounts[accountNumber]["balance"]))

    def deposit(self, accountNumber, depositAmount):
        oldBalance = self.activeSavingsAccounts[accountNumber]["balance"]
        newBalance = oldBalance + depositAmount
        self.activeSavingsAccounts[accountNumber]["balance"] = newBalance
        print(" ")
        print("You have deposited ${} into your account.".format(depositAmount))
        print(" ")

    def withdraw(self, accountNumber, withdrawalAmount):
        oldBalance = self.activeSavingsAccounts[accountNumber]["balance"]
        if oldBalance >= withdrawalAmount:
            newBalance = oldBalance - withdrawalAmount
            self.activeSavingsAccounts[accountNumber]["balance"] = newBalance
            print(" ")
            print("You have withdrawn ${} from your account.".format(withdrawalAmount))
            print(" ")
        else:
            print(" ")
            print("Error: The amount you requested to withdraw is less than your current available balance!")
            print(" ")

    # def checkActiveAccounts(self): ################
    #    print(self.activeSavingsAccounts) ##############


Bank = SavingsBank()

print(" ")
print("Welcome! ")
while True:
    print(" ")
    print("Main Menu: ")
    print("Enter 1 to create a new Savings Account")
    print("Enter 2 to access an existing Savings Account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice == 1:
        print("Now creating a new Savings Account...")
        print("Please enter the name you would like to be associated with your new Savings Account (no spaces):")
        customerName = input()
        print("Please enter the amount of your initial deposit to your new Savings Account: ")
        firstDeposit = int(input())
        newAccountNumber = Bank.createNewAccountNumber()
        Bank.createNewSavingsAccount(newAccountNumber, customerName, firstDeposit)
        print("Congratulations, {}! You have created a new Savings Account. Your account number is {}. Please keep this number for your records. Your current balance is ${}.".format(customerName, newAccountNumber, firstDeposit))
    elif userChoice == 2:
        print("Please enter the name associated with your Savings Account:")
        customerName = input()
        print("Please enter the 5-digit account number associated with your Savings Account:")
        customerAccountNumber = input()
        if customerAccountNumber in Bank.activeSavingsAccounts:
            if Bank.activeSavingsAccounts[customerAccountNumber]["name"] == customerName:
                print(" ")
                print("Hello, {}! ".format(customerName))
                while True:
                    print("Enter 1 to display your current balance")
                    print("Enter 2 to make a deposit")
                    print("Enter 3 to make a withdrawal")
                    print("Enter 4 to finish your session and exit to Main Menu")
                    userChoice2 = int(input())
                    if userChoice2 == 1:
                        print(" ")
                        Bank.displayAvailableBalance(customerAccountNumber)
                        print(" ")
                    elif userChoice2 == 2:
                        print(" ")
                        print("Please enter the amount you would like to deposit:")
                        depositAmount = int(input())
                        Bank.deposit(customerAccountNumber, depositAmount)
                    elif userChoice2 == 3:
                        print(" ")
                        print("Please enter the amount you would like to withdraw:")
                        withdrawalAmount = int(input())
                        Bank.withdraw(customerAccountNumber, withdrawalAmount)
                    elif userChoice2 == 4:
                        print("Session ended. Goodbye, {}. Returning to Main Menu now...".format(customerName))
                        break
                    else:
                        print("{}, please enter a number 1-4:".format(customerName))
                        print("Enter 1 to make a deposit")
                        print("Enter 2 to make a withdrawal")
                        print("Enter 3 to display your current balance")
                        print("Enter 4 to finish your session and exit to Main Menu")
            else:
                print("The information that you entered did not match our records. Returning to the Main Menu now...")
        else:
            print("The information that you entered did not match our records. Returning to the Main Menu now...")
    elif userChoice == 3:
        quit()
    else:
        print("Please enter a number 1-3:")
        print("Enter 1 to create a new Savings Account")
        print("Enter 2 to access an existing Savings Account")
        print("Enter 3 to exit")
