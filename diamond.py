class A:
    def method(self):
        print("This method belongs to class A")
    pass

class B(A):
    def method(self):
        print("This method belongs to class B")
    pass

class C(A):
    def method(self):
        print("This method belongs to class C")
    pass

class D(B, C): # order of inheritance matters: Method Resolution Order (MRO)
    pass

d = D()
d.method()


# best to stay away from multiple inheritance!!
