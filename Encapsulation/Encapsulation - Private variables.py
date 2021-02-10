"""
We can access and modify class private variables only from inside a class
we cant access or modify private methods of class from outside the class
"""


class Car:
    __maxSpeed = 0
    __name = ''

    def __init__(self):
        self.__maxSpeed = 200
        self.__name = 'BMW'

    def drive(self):
        print("Driving")
        print("maxSpeed value before calling setSpeed method: " + str(self.__maxSpeed))

    def setSpeed(self, speed):
        self.__maxSpeed = speed
        print("Current Max speed after calling setSpeed() is: " + str(self.__maxSpeed))


if __name__ == '__main__':
    c1 = Car()
    c1.drive()
    print()

    c1.setSpeed(500)

    print()
    # another way of accessing private method from outside the class not a good practice
    print("accessing private valiable from outside a clas:", c1._Car__maxSpeed)
