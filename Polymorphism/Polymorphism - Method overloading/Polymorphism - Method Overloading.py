"""
Method Overloading:

Method Overloading is the class having methods that are the same name with different arguments.
Arguments different will be based on a number of arguments and types of arguments.
It is used in a single class.
It is also used to write the code clarity as well as reduce complexity.
"""


# def Hello_emp(employeeName=None):
#     if employeeName is None:  # if we pass value then execute else part or if part if part will be executed
#         print("Hello")
#     else:
#         print("Hello " + employeeName)
#
#
# def class_area(a=None, b=None):
#     if a is not None and b is not None:
#         print("Area of rectangle is: " + str(a * b))
#     elif a is not None:
#         print("Area of triangle is: " + str(a * a))
#     else:
#         print("Nothing to print")

"""
The above code are lengthy because of if and else statements so lets implement method overloading using dispatch

In Backend, Dispatcher creates an object which stores different implementation and on runtime, it selects the 
appropriate method as the type and number of parameters passed.
"""
from multipledispatch import dispatch


@dispatch(int, int)
def add(a, b):
    print(a + b)


@dispatch(int, float, int)
def add(a, b, c):
    print(a + b + c)


if __name__ == '__main__':
    # Hello_emp()
    # Hello_emp('Gagan')

    # class_area()
    # class_area(9)
    # class_area(5)
    add(5, 4)
    add(1, 2.0, 3)
