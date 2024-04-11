# SHIKHAR UPADHYAY
# QUESTION 
class ParentClass:
    def __init__(self):
        self.__private_field1 = "Private Field 1"
        self.__private_field2 = "Private Field 2"

    def __private_method(self):
        print("This is a private method")

    def print_fields(self):
        print("Private Field 1:", self.__private_field1)
        print("Private Field 2:", self.__private_field2)
        self.__private_method()

    def get_private_field1(self):
        return self.__private_field1


class SubClass(ParentClass):
    def access_private_fields(self):
        # Trying to access private fields from the subclass
        # This will result in an AttributeError
        # Uncomment this line to see the error
        # print("Private Field 1 in Subclass:", self.__private_field1)

        # Accessing private fields through a method of the superclass
        print("Private Field 1 in Subclass:", self.get_private_field1())

    def access_private_method(self):
        # Trying to call private method from the subclass
        # This will result in an AttributeError
        # Uncomment this line to see the error
        # self.__private_method()

        # Accessing private method through a method of the superclass
        self.print_fields()


def main():
    # Creating an instance of the parent class
    parent_obj = ParentClass()

    # Accessing private fields and method of parent class
    print("Private Fields and Method in Parent Class:")
    parent_obj.print_fields()
    print()

    # Creating an instance of the subclass
    subclass_obj = SubClass()

    # Accessing private fields and method of parent class from subclass
    print("Private Fields and Method in Subclass:")
    subclass_obj.access_private_fields()
    print()

    # Trying to access private fields and method of subclass
    # Uncomment these lines to see the error
    # print("Private Fields in Subclass:", subclass_obj.__private_field1)
    # subclass_obj.__private_method()


if __name__ == "__main__":
    main()










