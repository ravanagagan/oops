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
7. Twist is if we call parent from 'Class C' Then only init of Class is getting called[why means it will always starts
        from left to right]
8. This is what 'Method Resolution Order(MRO)' means
9. if we create multiple methods in different super classes with same name
    9-a. if we call super()__init__ then obviously it will call 'class A __init__()'
10.  By using 'super()' method we can also call the super class method, to represent super class we will use
        super method
"""


class A:
    def __init__(self):
        print("This is init of A class")

    def feature1(self):
        print("This is 1st-A feature")

    def feature2(self):
        print("This is 2nd feature")


class B:
    def __init__(self):
        print("This is init of B class")

    def feature1(self):
        print("This is 1st-A feature")

    def feature4(self):
        print("This is 4th feature")


class C(A, B):  # here class C inheriting all the features from class B and class A
    def __init__(self):
        super().__init__()
        print("This is init of C class")

    def feat(self):
        super().feature4()  # by using super method we can also call the super class method


if __name__ == '__main__':
    c1 = C()  # calls Class A init method
    c1.feature1()
    c1.feat()
