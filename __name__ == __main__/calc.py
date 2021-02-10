# see "first module" print statment is not displayed in this class because demo is not first module in this file
# when demo imported to other class, imported class will become the first module and demo becomes library


import demo

print()
print("Calc file data")
print("Hello calc")
print(__name__)
