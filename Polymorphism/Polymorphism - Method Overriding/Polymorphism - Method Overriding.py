"""
Read from the Book

if child class don't have the show() method called then child class will go and search in parent, if show() method is
present it will call that method
if child and parent both have show() method then child class always overrides parent class. so child class show() will
be called
"""


# in below example child class calls parent class show()


class A:
    def show(self):
        print("A class Show")


class B(A):
    pass


b = B()
print("First Example")
b.show()  # "A class Show"
print()


# in below example child class have show() method so it will override parent class show() method
class A:
    def show(self):
        print("A class Show")


class B(A):
    def show(self):
        print("B class Show")


b = B()
print("Second Example")
b.show()  # "B class Show"
