# here if we execute it will print First module in imported module it wont display

print("Imported Demo to calc: [imported from '" + __name__ + "' module]")  # it will print the module name in imported class
# in this file if it will display __main__ because it is a first module


if __name__ == '__main__':
    print("First module")
