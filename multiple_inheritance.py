class OperatingSystem:
    multitasking = True
    name = "Mac OS"

class Apple:
    name = "Apple"
    website = "www.apple.com"

class MacBook(OperatingSystem, Apple): # order matters
# if there's a conflict in attributes in inheritated classes, the first class wins
    def __init__(self):
        if self.multitasking == True:
            print("This is a multitasking system. Visit {} for more details".format(self.website)) # this will be True
            print("Name:", self.name) # this will be Mac OS

macbook = MacBook()
