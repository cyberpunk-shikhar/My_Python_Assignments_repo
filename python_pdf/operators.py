# NAME :- SHIKHAR UPADHYAY
# Question :-2
# Write a function for arithmetic operators(+,-,*,/)

#plus(+) operator
a =4
b = 2
addition =a+b
print("The sum of",addition)

#minus(-) operator
subtract=a-b
print("the subtract is ",subtract)

#multiply (x) operator.
product= a*b
print ("The product of",product)


#division(/) operator
quotient= a/b
remainder= a%b
print("The quotient and remainder are:")
print(quotient,"and",remainder)


print()

# Question :- 2
# Write a method for increment and decrement operators(++, --)

def increment(value):
       return value + 1

def decrement(value):
        return value - 1

# Let take Example usage:
x = 15
print("Original value of x:", x)

# Increment x
x = increment(x)
print("After increment, value of x:", x)

# Decrement x
x = decrement(x)
print("After decrement, value of x:", x)

print()

# Qyestion :- 3
# Write a program to find the two numbers equal or not.


def equal(num1, num2):
    """
    Function to check if two numbers are equal.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        bool: True if the numbers are equal, otherwise false.
    """
    if num1 == num2:
        return True
    else:
        return False

# Taking inoput value from the user
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

if equal(number1, number2):
    print("The numbers", number1, "and", number2, "are equal.")
else:
    print("The numbers", number1, "and", number2, "are not equal.")

print()

# Question :- 4
# Program for relational operators (<,<==, >, >==)

def compare_numbers(num1, num2):
    """
    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        str: A string indicating the result of the comparison.
    """
    if num1 < num2:
        return f"{num1} is less than {num2}"
    elif num1 <= num2:
        return f"{num1} is less than or equal to {num2}"
    elif num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 >= num2:
        return f"{num1} is greater than or equal to {num2}"
    else:
        return "Invalid comparison"

# Taking value, from the user.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = compare_numbers(number1, number2)
print(result)


print()

# Question :- 5
# Print the smaller and larger number

def Smaller_Larger(num1, num2):
   
    if num1 < num2:
        return num1, num2
    elif num1 > num2:
        return num2, num1
    else:
        return "Both numbers are equal"

# Example usage:
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

smaller, larger = Smaller_Larger(number1, number2)
print("Smaller number:", smaller)
print("Larger number:", larger)


