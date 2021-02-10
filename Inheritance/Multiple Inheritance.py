"""
This is Mulyiple Inheritance
'Class C' Inheriting all the features from 'Class B' and 'Class A'
"""


class A:
    def feature1(self):
        print("This is 1st feature")

    def feature2(self):
        print("this is 2nd feature")


class B:  # here class B inheriting all the features from class A
    def feature3(self):
        print("This is 3rd feature")

    def feature4(self):
        print("This is 4th feature")


class C(A, B):  # here class C inheriting all the features from class B
    def feature5(self):
        print("This is 4th feature")

    def feature6(self):
        print("This is 5th feature")


if __name__ == '__main__':
    a_obj = A()
    print("Parent class features access from parent object: ", end='')
    a_obj.feature1()
    print("Parent class features access from parent object: ", end='')
    a_obj.feature1()


    print()
    b_obj = B()
    print("Parent class features access from parent object: ", end='')
    b_obj.feature3()
    print("Parent class features access from parent object: ", end='')
    b_obj.feature4()

    print()
    c_obj = C()
    print("Parent class features access from child object: ", end='')
    c_obj.feature1()
    print("Parent class features access from child object: ", end='')
    c_obj.feature2()
    print("Parent class features access from child object: ", end='')
    c_obj.feature3()
    print("Parent class features access from child object: ", end='')
    c_obj.feature4()
    print("Child class features access from child object: ", end='')
    c_obj.feature5()
    print("Child class features access from child object: ", end='')
    c_obj.feature6()