# SHIKHAR UPADHYAY
# Questio -1
# Write a program to generate Arithmetic Exception without exception handling

result = 10 / 0  # This line will raise an ArithmeticError

# This line will not be executed because an exception will be raised above
print("This line will not be printed.")

print()

# Questio -2
#  Handle the Arithmetic exception using try-catch block

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught an Arithmetic Exception: Division by zero!")

print()

# Questio -3
# Write a method which throws exception, Call that method in main class without try block

# Method that throws exception
def divide_by_zero():
    result = 10 / 0

# Call the method without try block (exception will propagate)
divide_by_zero()

print()

# Questio -4
# Write a program with multiple catch blocks

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Invalid data type provided!")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Division result:", result)
    finally:
        print("Division operation complete.")


if __name__ == "__main__":
    # Test cases
    divide_numbers(10, 2)  # No exception will be raised
    divide_numbers(10, 0)  # ZeroDivisionError will be caught
    divide_numbers(10, "2")  # TypeError will be caught
    divide_numbers("10", 2)  # Exception will be caught

print()


# Question -5
# Write a program to throw exception with your own message

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")


if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        validate_age(age)
        print("Valid age entered:", age)
    except ValueError as e:
        print("Error:", e)

print()


# Question -6
# Write a program to create your own exception

class MyCustomException(Exception):
    def __init__(self, message="Default error message"):
        self.message = message
        super().__init__(self.message)

if __name__ == "__main__":
    try:
        # Raise your custom exception with a custom message
        raise MyCustomException("This is a custom exception message")
    except MyCustomException as e:
        print("Custom Exception caught:", e.message)

print()

# Question -7
# Write a program with finally block

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Division result:", result)
    finally:
        print("Finally block: Division operation complete.")


if __name__ == "__main__":
    # Test cases
    divide_numbers(10, 2)  # No exception will be raised
    divide_numbers(10, 0)  # ZeroDivisionError will be caught

print()

# Question -8
# Write a program to generate Arithmetic Exception

def generate_arithmetic_exception():
    result = 10 / 0  # This line will raise an ArithmeticError

if __name__ == "__main__":
    generate_arithmetic_exception()

print()

# Question -9
# Write a program to generate FileNotFoundException

def generate_file_not_found_exception():
    try:
        # Attempting to open a non-existent file
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found!")
    else:
        print("File read successfully:", content)

if __name__ == "__main__":
    generate_file_not_found_exception()

print()

# Question -10
# Write a program to generate ClassNotFoundException

def generate_class_not_found_exception():
    try:
        # Attempting to import a non-existent module
        import non_existent_module
    except ImportError:
        print("Module not found!")
    else:
        print("Module imported successfully:", non_existent_module)

if __name__ == "__main__":
    generate_class_not_found_exception()


print()

# Question -11
# Write a program to generate IOException

def generate_io_exception():
    try:
        # Attempting to open a file in write mode without read permissions
        with open("/etc/shadow", "w") as file:
            file.write("Test")
    except PermissionError as e:
        print("Permission denied:", e)
    except FileNotFoundError as e:
        print("File not found:", e)
    except OSError as e:
        print("OS error:", e)
    else:
        print("File write operation completed successfully.")

if __name__ == "__main__":
    generate_io_exception()


print()

# Question-12
# Write a program to generate NoSuchFieldException

class MyClass:
    def __init__(self):
        self.attribute = "value"

def generate_no_such_field_exception():
    try:
        obj = MyClass()
        # Attempting to access a non-existent attribute
        print(obj.non_existent_attribute)
    except AttributeError as e:
        print("Attribute not found:", e)
    else:
        print("Attribute access successful.")

if __name__ == "__main__":
    generate_no_such_field_exception()









