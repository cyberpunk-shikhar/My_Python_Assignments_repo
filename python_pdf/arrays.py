# SHIKHAR UPADHYAY
# QUESTION - 1
# Write a function to add integer values of an array.

def add_array(array):

    total_sum = 0
    for element in array:
        total_sum += element
    return total_sum

my_array = [14, 15, 16, 17, 18]
array_sum = add_array(my_array)
print("Sum of our array is:", array_sum)


print()

# QUESTION -2
#Write a function to calculate the average value of an array of integers


def calculate_average(array):
  
    total_sum = sum(array)
    array_length = len(array)
    
    if array_length == 0:
        return 0  # Avoid division by zero if the array is empty
    else:
        return total_sum / array_length

# Let Take Example
my_array = [1, 2, 3, 4, 5]
average_value = calculate_average(my_array)
print("Average value of the array:", average_value)

print()

# QUESTION -3
# Write a program to find the index of an array element.

def find_index(arr, target):
    
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example is:
my_array = [20, 30, 40, 50, 60]
target_element = 40

index = find_index(my_array, target_element)

if index != -1:
    print("Index of", target_element, "in the array:", index)
else:
    print(target_element, "not found in the array.")

print()

# QUESTION -4
# Write a function to test if array contains a specific value.

def contains_value(arr, target):
  
    for element in arr:
        if element == target:
            return True
    return False

# Example is:
my_array = [10, 20, 30, 40, 50]
target_value = 30

if contains_value(my_array, target_value):
    print("The array contains", target_value)
else:
    print("The array does not contain", target_value)

print()


# QUESTION -5
# Write a function to remove a specific element from an array.

def remove_element(arr, target):
 
    arr.remove(target)
    return arr

# Example usage:
my_array = [10, 20, 30, 40, 50]
element_to_remove = 30

remove_element(my_array, element_to_remove)
print("Array after removing", element_to_remove, ":", my_array)

print()

# QUESTION -6
# Write a function to copy an array to another array

def copy_array(arr):
   
    return arr[:]

# Example is:
orgnl_array = [10, 20, 30, 40, 50]

# Copy the original array to a new array
copied_array = copy_array(orgnl_array)

print("Original array:", orgnl_array)
print("Copied array:", copied_array)

print()

# QUESTION -7
# Write a function to insert an element at a specific position in the array

def insert_element(arr, element, position):
 
    # Insert the element at the specified position using list slicing
    return arr[:position] + [element] + arr[position:]

# Example usage:
my_array = [10, 20, 30, 40, 50]
element_to_insert = 35
insert_position = 4

result_array = insert_element(my_array, element_to_insert, insert_position)
print("Array after inserting", element_to_insert, "at position", insert_position, ":", result_array)

# QUESTION -8
# Write a function to find the minimum and maximum value of an array.

def find_min_max(arr):
  
    min_value = min(arr)
    max_value = max(arr)
    return min_value, max_value

# Example usage:
my_array = [10, 20, 5, 30, 40, 15]

min_value, max_value = find_min_max(my_array)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

print()

# QUESTION -9
# Write a function to reverse an array of integer values

def reverse_array(arr):
 
    return arr[::-1]

# Example:
my_array = [10, 20, 30, 40, 50]

reversed_array = reverse_array(my_array)
print("Original array:", my_array)
print("Reversed array:", reversed_array)

print()

# Question -10
# Write a function to find the duplicate values of an array

def find_duplicates(arr):
 
# Create a dictionary to store element frequencies
    frequency = {}
    
# Initialize an empty list to store duplicate values
    duplicates = []

# Iterate through the array and update frequencies in the dictionary
    for element in arr:
        if element in frequency:
            duplicates.append(element)
        else:
            frequency[element] = 1

    return duplicates

# Example:
my_array = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1, 9, 10, 1]

duplicate_values = find_duplicates(my_array)
print("Duplicate values:", duplicate_values)

print()

# Question -11
# Write a program to find the common values between two arrays

def find_common_values(arr1, arr2):

    set1 = set(arr1)
    set2 = set(arr2)
    return set1.intersection(set2)

# Example:
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

common_values = find_common_values(array1, array2)
print("Common values between the arrays:", common_values)

print()


# Question -12
# Write a method to remove duplicate elements from an array.

def remove_duplicates(arr):
  
    return list(set(arr))

# Example:
my_array = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1]

unique_elements = remove_duplicates(my_array)
print("Array after removing duplicates:", unique_elements)

print()


# Question -13
# Write a method to find the second largest number in an array

def second_largest(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    if len(unique_elements) < 2:
        return 
    return unique_elements[-2]

# 
array13 = [10, 20, 5, 30, 40]
print("Second largest number:", second_largest(array13))

print()

# Question -14
# Write a method to find the second largest number in an array

def second_smallest(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    if len(unique_elements) < 2:
        return 
    return unique_elements[1]

array14 = [10, 20, 5, 30, 40]
print("Second smallest number:", second_smallest(array14))

print()

# Question-15
# Write a method to find number of even number and odd numbers in an array

def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

# Example usage:
array15 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count_even_odd(array15)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)

print()

# Question -16
# Write a function to get the difference of largest and smallest value.

def get_difference(arr):
 
    if not arr:  # Check if the array is empty
        return None

    max_value = max(arr)
    min_value = min(arr)

    return max_value - min_value

# Example:
my_array = [10, 5, 20, 15, 30, 25]

difference = get_difference(my_array)
if difference is not None:
    print("Difference between largest and smallest values:", difference)
else:
    print("Array is empty.")

print()

# Question - 17
# Write a method to verify if the array contains two specified elements(12,23).


def contains_elements(arr):
  
    return 12 in arr and 23 in arr

# Example:
my_array = [10, 20, 12, 30, 40, 23, 50]

if contains_elements(my_array):
    print("The array contains both 12 and 23.")
else:
    print("The array does not contain both 12 and 23.")

print()

# Question -18
# Write a program to remove the duplicate elements and return the new array


def remove_duplicates(arr):

    return list(set(arr))

# Example:
my_array = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1]

unique_array = remove_duplicates(my_array)
print("Array after removing duplicates:", unique_array)






