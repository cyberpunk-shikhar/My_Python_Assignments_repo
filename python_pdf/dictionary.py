# SHIKHAR UPADHYAY
# Question -1
# Create a Dictionary with at least 5 key value pairs of the Student ID and Name

# Creating a dictionary of student IDs and names
student_dict = {
    101: "SHIKHAR",
    102: "KAPIL",
    103: "ANKIT",
    104: "MANOJ",
    105: "MOHIT"
}

# Printing the dictionary
print("Student Dictionary:", student_dict)

print()

# Question -1.1
# 1.1. Adding values to the dictionary
student_dict[106] = 'Markan'
print("1.1. After Adding New Value:")
print(student_dict)

print()

# Question -1.2
# 1.2. Updating values in the dictionary
student_dict[104] = 'Luka'
print("\n1.2. After Updating Value:")
print(student_dict)

print()

# Question -1.3
# 1.3. Accessing a value in the dictionary
print("\n1.3. Accessing Value for Student ID 102:")
print(student_dict[102])


print()

# Question -1.4
# 1.4. Creating a nested dictionary (Student ID, Name, and Age)

nested_dict = {
    101: {'Name': 'SHIKHAR', 'Age': 20},
    102: {'Name': 'KAPIL', 'Age': 21},
    103: {'Name': 'UTSAV', 'Age': 22}
}


print()

# Question -1.5
# 1.5. Accessing values of the nested dictionary

print("\n1.5. Accessing Values of Nested Dictionary:")
for student_id, details in nested_dict.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {details['Name']}")
    print(f"Age: {details['Age']}")

print()

# Question -1.6
# 1.6. Printing keys present in a particular dictionary
print("\n1.6. Keys Present in the Student Dictionary:")
for key in student_dict.keys():
    print(key)


print()

# Question -1.7
# 1.7. Deleting a value from the dictionary
del student_dict[106]
print("\n1.7. After Deleting Value:")
print(student_dict)
