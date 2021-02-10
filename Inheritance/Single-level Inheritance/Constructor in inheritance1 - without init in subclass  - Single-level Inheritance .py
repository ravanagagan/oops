"""
Constructor in Inheritance
1. In this we are creating the object of child class
2. if we create the object of Subclass it will first try to find init in sub class if it is not-found then it will
    call init of super class
"""


class A:
    def __init__(self):
        print("Init of A class")

    def feature1(self):
        print("This is 1st feature")

    def feature2(self):
        print("This is 2nd feature")


class B(A):
    def feature3(self):
        print("This is 3rd feature")

    def feature4(self):
        print("This is 4th feature")


if __name__ == '__main__':
    b1 = B()