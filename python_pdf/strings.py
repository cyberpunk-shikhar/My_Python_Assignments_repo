# SHIKHAR UPADHYAY
# Question -1
# Different ways creating a string

# Using single quotes
string1 = 'Hello, World!'

# Using double quotes
string2 = "Hello, World!"

# Using triple quotes for multi-line strings
string3 = '''This is a
multi-line
string'''

print(string1)
print(string2)
print(string3)

print()

# Question -2
# Concatenating two strings using + operator

str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print(result)

print()

# Question -3
# Finding the length of the string

my_string = "Hello, World!"
string_length = len(my_string)
print("Length of the string:", string_length)

print()

# Question -4
# Extract a string using Substring

my_string = "Hello, World!"
substring = my_string[7:12]  # Extracts substring from index 7 to index 11 (exclusive)
print("Substring:", substring)

print()

# Question -5
# Searching in strings using index()

my_string = "Hello, World!"
substring = "World"
index = my_string.index(substring)
print("Index of the substring:", index)

print()

# Question -6
# Matching a String Against a Regular Expression With matches()

import re

# Regular expression pattern
pattern = r'Hello'

# Input string
input_string = "Hello, World!"

# Check if the input string matches the pattern
match = re.match(pattern, input_string)

if match:
    print("String matches the pattern.")
else:
    print("String does not match the pattern.")

print()

# Question -7
# Comparing strings

string1 = "Hello"
string2 = "World"

if string1 == string2:
    print("Strings are equal")
else:
    print("Strings are not equal")

print()

# Question -8
# startsWith(), endsWith() and compareTo()

def starts_with(string, prefix):
    return string[:len(prefix)] == prefix

my_string = "Hello, World!"
prefix = "Hello"

if starts_with(my_string, prefix):
    print("String starts with the prefix.")
else:
    print("String does not start with the prefix.")

def ends_with(string, suffix):
    return string[-len(suffix):] == suffix

my_string = "Hello, World!"
suffix = "World!"

if ends_with(my_string, suffix):
    print("String ends with the suffix.")
else:
    print("String does not end with the suffix.")

string1 = "apple"
string2 = "banana"

if string1 == string2:
    print("Strings are equal")
elif string1 < string2:
    print("string1 comes before string2")
else:
    print("string1 comes after string2")

print()

# Question -9
# Trimming strings with strip()

string = "  Hello, World!  "

# Removing leading and trailing whitespace
trimmed_string = string.strip()

print("Original string:", string)
print("Trimmed string:", trimmed_string)

print()

# Question -10
# Replacing characters in strings with replace()

string = "Hello, World!"

# Replace "Hello" with "Hi"
new_string = string.replace("World", "SHIKHAR")

print("Original string:", string)
print("New string:", new_string)

print()

# Question -11
# Splitting strings with split()

str = "Hello, World!"

# Splitting the string by comma and space
split_str = string.split(", ")

print("Original string:", str)
print("Split string:", split_str)

print()

# Question -12
# Converting integer objects to Strings

integer_value = 42
string_value = str(integer_value)
print("String representation:", string_value)
print("Type of string representation:", type(string_value))


# Question -13
# Converting to uppercase and lowercase

my_string = "Hello, World!"

# Convert to uppercase
uppercase_string = my_string.upper()
print("Uppercase:", uppercase_string)

# Convert to lowercase
lowercase_string = my_string.lower()
print("Lowercase:", lowercase_string)

