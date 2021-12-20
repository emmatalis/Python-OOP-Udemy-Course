# implement a library management system which will handle the following tasks:
# customer should be able to display all the books available in the library
# handle the process when a customer requests to borrow a book
# update the library collection when the customer returns a book

# class = library
# layers of abstraction => display available books, to lend a book, to add a book

# class = customer
# layers of abstraction => to request a book, to return a book

class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
        print()

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book.")
            print()
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list.")
            print()

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank you!")
        print()

class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of a book which you are returning: ")
        self.book = input()
        return self.book

library = Library(["Think and Grow Rich", "Who Will Cry When You Die", "For One More Day"])
customer = Customer()

while True:
    print("Menu: ")
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userChoice = int(input())

    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()
    else:
        print("Please enter a number 1-4")
