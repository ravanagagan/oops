"""
This is Single level Inheritance
'Class B' Inheriting all the features from 'Class A'
"""


class A:
    def feature1(self):
        print("This is 1st feature")

    def feature2(self):
        print("this is 2nd feature")


class B(A):  # here class B inheriting all the features from class A
    def feature3(self):
        print("This is 3rd feature")

    def feature4(self):
        print("This is 4th feature")


if __name__ == '__main__':
    a_obj = A()
    print("Parent class features access from parent object: ", end='')
    a_obj.feature1()
    print("Parent class features access from parent object: ", end='')
    a_obj.feature1()

    b_obj = B()
    print("Parent class features access from child object: ", end='')
    b_obj.feature1()
    print("Parent class features access from child object: ", end='')
    b_obj.feature2()
    print("Child class features access from child object: ", end='')
    b_obj.feature3()
    print("Child class features access from child object: ", end='')
    b_obj.feature4()