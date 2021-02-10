"""
Encapsulation:
    Encapsulation is nothing but a wrapping broth data member and member functions together as single unit
Data Encapsulation is also known as data hiding, is the mechanism whereby the implementation details of the class
    are kept hidden from the user
"""

class Car:
    def __init__(self):
        self.__hiddenCar()  # we can access method only from inside a class, it will give output

    def blackCar(self):
        print("Driving")

    def __hiddenCar(self):
        print("This car is hidden")


if __name__ == '__main__':
    c1 = Car()
    c1.blackCar()

    print()
    # this is not a good practice but we can access the private method like this
    print("Not a good practice bro another way to access private method from outside a class")
    c1._Car__hiddenCar()