"""
Constructor in Inheritance
1. In this we are creating the object of child class
2. We will create __init__() method in subclass as well
3. if we create the object of Subclass it will first try to find init in sub class if it is not-found then it will
    call init of super class
4. if child class find init method in subclass then it wont class init method present in superclass
5. we can call both' __init__()' by 'calling __init__() of super class' from '__init__() method of child class'
6. Syntax to call parent class init from child init method
    def __init__(self):  # child class init
        super().__init__()
        print("Init of B class")
"""


class A:
    def __init__(self):
        print("Init of A class")

    def feature1(self):
        print("This is 1st feature")

    def feature2(self):
        print("This is 2nd feature")


class B(A):
    def __init__(self):
        super().__init__()
        print("Init of B class")

    def feature3(self):
        print("This is 3rd feature")

    def feature4(self):
        print("This is 4th feature")


if __name__ == '__main__':
    b1 = B()