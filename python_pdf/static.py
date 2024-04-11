# SHIKHAR UPADHYAY
# Question 1
# Define a static variable and access that through a class

class MyClass:
    static_variable = "Hello, I am a static variable!"

# Accessing the static variable through the class
print(MyClass.static_variable)

print()

# Question -2
# Define a static variable and access that through a instance

class MyClass:
    static_variable = "This is a static variable!"

# Create an instance of MyClass
my_instance = MyClass()

# Accessing the static variable through the instance
print(my_instance.static_variable)

print()


# Question -3
# Define a static variable and change within the instance

class MyClass:
    static_variable = "Hello, I am a static variable!"

# Create an instance of MyClass
my_instance = MyClass()

# Accessing the static variable through the instance
print("Before change - static_variable value through instance:", my_instance.static_variable)

# Change the static variable through the instance
my_instance.static_variable = "I am changed through an instance!"

# Accessing the static variable through the instance after change
print("After change - static_variable value through instance:", my_instance.static_variable)

# Accessing the static variable directly through the class
print("Before change - static_variable value through class:", MyClass.static_variable)

# Change the static variable directly through the class
MyClass.static_variable = "I am changed directly through the class!"

# Accessing the static variable through the instance after change
print("After change - static_variable value through class:", MyClass.static_variable)

print()

# Question -4
# Define a static variable and change within the class

class MyClass:
    static_variable = "Initial value"

    @classmethod
    def change_static_variable(cls, new_value):
        cls.static_variable = new_value

# Accessing the static variable before change
print("Before change - static_variable value:", MyClass.static_variable)

# Changing the static variable within the class
MyClass.change_static_variable("New value")

# Accessing the static variable after change
print("After change - static_variable value:", MyClass.static_variable)




