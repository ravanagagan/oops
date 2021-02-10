"""
Constructor in Inheritance
1. In this we are creating the object of child class
2. if we create the object of Subclass it will first try to find init in sub class if it is not-found then it will
    call init of super class
"""


class A:
    def feature1(self):
        print("This is 1st feature")

    def feature2(self):
        print("This is 2nd feature")


class B:
    def feature3(self):
        print("This is 3rd feature")

    def feature4(self):
        print("This is 4th feature")


class C(A, B):  # here class C inheriting all the features from class B and class A
    def __init__(self):
        print("This is init of C class")

    def feature5(self):
        print("This is 4th feature")

    def feature6(self):
        print("This is 5th feature")


if __name__ == '__main__':
    c1 = C()