# SHIKHAR UPADHYAY
"""Question- 1. Create a program to create two class.
1.1. Create a constructor and a method for each class
1.2. Create a __init__.py for adding all packages
1.3. Import the respective packages
1.4. Call each class by creating an object to it 
1.5. Create a program by all the above"""



class Class1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from Class1, {self.name}!")

class Class2:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome from Class2, {self.name}!")





# Create objects for Class1 and Class2
class1_obj = Class1("SHIKHAR")
class2_obj = Class2("UPADHYAY")

# Call methods of Class1 and Class2
class1_obj.greet()
class2_obj.welcome()
