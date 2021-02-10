"""
x = 5 -> 5 is a integer object, memory will be alloocated for that -> x is just a name for it
x = 'Gagan' -> 'Gagan' is a String object, memory will be alloocated for that -> x is just a name for it
note: We dont have specific type for X


No matter which class object this is what only matters is object, and object's class must contain the calling method
"""


class PyCharm:
    def execute(self):  # we will represent behaviours in methods so if that method is present then its duck
        print("Compile")
        print("Execute")


class MyEditor:
    def execute(self):
        print("Compile")
        print("Execute")
        print("Spelling Correction")
        print("Conventions")


class Laptop:
    def code(self, ide):  # here ide is object of any class only matter is object's class must contain execute method
        ide.execute()


p1 = PyCharm()
m1 = MyEditor()

l1 = Laptop()

print("Pycharm Editor Features")
l1.code(p1)
print()

print("MyEditor Editor Features")
l1.code(m1)