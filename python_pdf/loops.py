# NAME - SHIKHAR UPADHYAY
# QUESTION -1
# Write a program to print “Bright IT Career” ten times using for loop.


for i in range(10):
    print("Bright IT Career")

print()

# QUESTION -2
# Write a java program to print 1 to 20 numbers using the while loop.

# Initialize the variable to start from 1
num = 1

# Loop until num reaches 20
while num <= 20:
    print(num)
    num += 1  # Increment num by 1 in each iteration

print()


#QUESTION -3
# Program to equal operator and not equal operators

def equal_not_equal(num1, num2):
   
    if num1 == num2:
        return f"{num1} is equal to {num2}"
    elif num1 != num2:
        return f"{num1} is not equal to {num2}"

# LET TAKE EXAMPLE:
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

result = equal_not_equal(number1, number2)
print(result)

print()


# QUESTION -4
#  Write a program to print the odd and even numbers.

def odd_even(start, end):
  
    print("Even numbers:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

    print("\nOdd numbers:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

# Example:
start_num = int(input("Enter the start number of the range: "))
end_num = int(input("Enter the end number of the range: "))

odd_even(start_num, end_num)

print()


# QUESTION -5
# Write a program to print largest number among three numbers

def find_largest(num1, num2, num3):
   
    largest = num1  # Assuming num1 is the largest initially
    
    if num2 > largest:
        largest = num2
    
    if num3 > largest:
        largest = num3
    
    return largest

# Example usage:
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

largest_number = find_largest(number1, number2, number3)
print("The largest number among", number1, ",", number2, ", and", number3, "is:", largest_number)

print()

# Question -6
#  Write a program to print even number between 10 and 20 using while

num = 10

print("Even numbers between 10 and 20:")
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1


print()

# Question -7
# Write a program to print 1 to 10 using the do-while loop statement.

num = 1

# Execute the loop body at least once
while True:
    print(num)
    num += 1
    
    # Check if the condition is met to exit the loop
    if num > 10:
        break
print()


# Question -8
# Write a program to find Armstrong number or not

def is_armstrong_number(number):
   
# Convert the number to a string to find its length (number of digits)
    num_str = str(number)
    num_digits = len(num_str)
    
# Calculate the sum of digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
# Check if the sum is equal to the original number
    return armstrong_sum == number

# Example:
num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

print()

# Question -9
# Write a program to find the prime or not.

def is_prime(number):
   
# Prime numbers are greater than 1
    if number <= 1:
        return False
    
# Check divisibility by numbers from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Example:
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

print()

# Question -10
#  Write a program to palindrome or not.


def is_palindrome(s):
  
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

print()

# Question -11
# Program to check whether a number is EVEN or ODD using switch

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function with different numbers
num1 = 25
num2 = 9
num3 = 0

result1 = check_even_odd(num1)
result2 = check_even_odd(num2)
result3 = check_even_odd(num3)

print(f"{num1} is {result1}")
print(f"{num2} is {result2}")
print(f"{num3} is {result3}")

print()

# Question -11 taking input from the user from the user
# Program to check whether a number is EVEN or ODD using switch


def check_even_odd(num):
   
    return {
        0: "Even",
        1: "Odd"
    }[num % 2]

# Example:
number = int(input("Enter a number: "))

result = check_even_odd(number)
print("The number is", result)

print()

# Question -12
#  Print gender (Male/Female) program according to given M/F using switch

def print_gender(gender):
    if gender == 'M':
        print("Gender: Male")
    elif gender == 'F':
        print("Gender: Female")
    else:
        print("Invalid input")

# Test the function with different inputs
input1 = 'M'
input2 = 'F'
input3 = 'X'  # Invalid input

print_gender(input1)
print_gender(input2)
print_gender(input3)




