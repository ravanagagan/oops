"""
In computer programming, operator overloading, sometimes termed operator ad hoc polymorphism, is a specific case of
polymorphism, where different operators have different implementations depending on their arguments.
Operator overloading: Operator overloading means operator remains same but operands will change

we can add two integers -> 5 + 6
we can add two strings -> 'Gagan' + 'Chandan'
we can add ont integer and one float - > 5 + 7.0

whatever happens in python it happens with the hep of python
a = 5
b = 6
print(a + b) -> internally this will be converted like this -> [int.__add__(a, b)]

Python operators work for built-in classes. But the same operator behaves differently with different types. For example,
the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

This feature in Python that allows the same operator to have different meaning according to the context is called
operator overloading.
"""


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        first = self.m1 + other.m1
        second = self.m2 + other.m2
        return first + second

    def __gt__(self, other):
        first = self.m1 + self.m2
        second = other.m1 + other.m2
        if first > second:
            return True
        else:
            return False

    def __str__(self):
        # we can do "return self.m1, self.m2" but we will get "TypeError: __str__ returned non-string (type tuple)"
        return "({}, {})".format(self.m1, self.m2)


if __name__ == '__main__':
    s1 = Student(60, 20)
    s2 = Student(32, 45)

    # returning complete total
    print("Addition of objects")
    print(s1 + s2)  # this wont work if we don't have add method in class

    print()
    print("Greater Than Operator Result:- ")
    if s1 > s2:
        print("s1 wins")
    else:
        print("s2 wins")
    print()

    # if we print a then it is printing value not address. internally it is calling print(a.__str__())
    a = 9
    print("Value of 'A' is: ", a)

    print()
    # it will print address of s1 object so we need to overload __str__ method
    print("Value of 's1' object is: ", s1)