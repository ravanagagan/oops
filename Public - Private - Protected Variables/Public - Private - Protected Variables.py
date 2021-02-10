"""
Public Members

Public members (generally methods declared in a class) are accessible from outside the class. The object of the same
class is required to invoke a public method. This arrangement of private instance variables and public methods ensures
the principle of data encapsulation.
All members in a Python class are public by default. Any member can be accessed from outside the class environment.

In fact, this doesn't prevent instance variables from accessing or modifying the instance. You can still perform the
following operations:
"""

# class Student:
#     schoolName = 'ABC'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# if __name__ == '__main__':
#     std = Student('Gagan', 23)
#     print("name of the student: " + std.name)
#     print("Age of the student:", std.age)
#
#     print("School name:", std.schoolName)
#
#     std.age = 25
#     print("Age of the student after modified: ", std.age)


"""
Private Members

Python doesn't have any mechanism that effectively restricts access to any instance variable or method. Python 
prescribes a convention of prefixing the name of the variable/method with a single or double underscore to emulate the
behavior of protected and private access specifiers.

The double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from 
outside the class. Any attempt to do so will result in an AttributeError:

Python performs name mangling of private variables. Every member with a double underscore will be changed 
to _object._class__variable. So, it can still be accessed from outside the class, but the practice should be refrained.
"""


# class Student:
#     __schoolName = 'XYZ School'  # private class attribute
#
#     def __init__(self, name, age):
#         self.__name = name  # private instance attribute
#         self.__salary = age  # private instance attribute
#
#     def __display(self):  # private method
#         print('This is private method.')
#
#     def publicMethod(self):
#         self.__schoolName = "Gagan School"
#         self.__display()
#         print("After Modification", self.__schoolName)
#
# if __name__ == '__main__':
#     std = Student("Bill", 25)
#     std.publicMethod()
#
#     print()
#     print("Trying to access private method and variables from outside class")
#     # std.__schoolName  # throw error
#     # std.__display()  # throw error
#
#     print("Way to access from outside the class, but not a good practice :", std._Student__schoolName)


"""
Protected Members
Protected members of a class are accessible from within the class and are also available to its sub-classes. 
No other environment is permitted access to it. This enables specific resources of the parent class to be 
inherited by the child class.

Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. 
This effectively prevents it from being accessed unless it is from within a sub-class.
"""


class Student:
    _schoolName = 'XYZ School'  # protected class attribute

    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute


if __name__ == '__main__':
    std = Student("Gagan", 22)
    print(std._name)  # accessing the protected variable from class instance

    std._name = "Chandan"  # modifying the protected variable from class instance
    print(std._name)