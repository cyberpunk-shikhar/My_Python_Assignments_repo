# NAME : SHIKHAR UPADHYAY
# ASSIGNMENT : 1
# Question :- Write a program to print your name.


name = "SHIKHAR UPADHYAY" 
print("Name:", name)

print()# user for space or white_space

# ASSIGNMENT : - 2
# Question :- Write a program for single line comment and multi-line comments

# This is a single-line comment
print("Hello, World!")  # This is also a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
"""
print("This is a multi-line comment example.")#This is multi-line comments

print()# user for space or white_space

#ASSIGNMENT :- 3
# Question :- Define variables for different Data Types int, Boolean, char, float, double and print on the console.


# Define variables for different data types
int_var = 10
boolean_var = True
char_var = 'a'
float_var = 3.14
double_var = 3.141592653589793238

# Print variables on the console
print("Integer Variable:", int_var)
print("Boolean Variable:", boolean_var)
print("Character Variable:", char_var)
print("Float Variable:", float_var)
print("Double Variable:", double_var)


print()# user for space or white_space.


#ASSIGNMENT :- 4
# Question :- Define the local and Global variables with the same name and print both variables and understand the scope of the variables

def my_function():
  # This is a local variable
  local_variable = 10

  # Print the value of the local variable
  print(local_variable)

# Call the function
my_function()

# Try to access the local variable outside of the function
# This will cause an error
print('local_variable')


# This is a global variable
global_variable = "I am a global variable"

def display_global():
    # Accessing the global variable inside this function
    print(global_variable)

def modify_global():
    global global_variable  # Declare that we're using the global variable
    global_variable = "I've been modified"

display_global() 
modify_global()
display_global()

