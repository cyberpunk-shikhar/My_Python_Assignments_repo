# SHIKHAR UPADHYAY
# Question -1
# Write two methods with the same name but different number of parameters of same type and call the methods

class MyClass:
    def method(self, arg1, arg2=None):
        if arg2 is not None:
            print("Method with two parameters:", arg1, arg2)
        else:
            print("Method with one parameter:", arg1)


if __name__ == "__main__":
    obj = MyClass()

    # Call the method with one parameter
    obj.method("Parameter1")

    # Call the method with two parameters
    obj.method("Parameter1", "Parameter2")

print()

# Question -2
# Write two methods with the same name but different number of parameters of different data type and call the methods

class MyClass:
    def method(self, arg1, arg2=None):
        if isinstance(arg2, int):
            print("Method with two parameters of different data types (int, int):", arg1, arg2)
        elif isinstance(arg2, str):
            print("Method with two parameters of different data types (int, str):", arg1, arg2)
        else:
            print("Method with one parameter:", arg1)


if __name__ == "__main__":
    obj = MyClass()

    # Call the method with one parameter
    obj.method("Parameter1")

    # Call the method with two parameters of different data types (int, int)
    obj.method("Parameter1", 123)

    # Call the method with two parameters of different data types (int, str)
    obj.method("Parameter1", "Parameter2")

print()

# SHIKHAR UPADHYAY
# Question -3
# Write two methods with the same name and same number of parameters of same type

class MyClass:
    def method(self, arg1, arg2=None):
        if arg2 is None:
            print("Method with one parameter:", arg1)
        else:
            print("Method with two parameters:", arg1, arg2)


if __name__ == "__main__":
    obj = MyClass()

    # Calling the method with one parameter
    obj.method("Parameter1")

    # Calling the method with two parameters
    obj.method("Parameter1", "Parameter2")

