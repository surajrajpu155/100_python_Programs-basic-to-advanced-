# 80. Write a program to read n elements into an array and print them.

# Step 1: Ask the user for the total number of elements (n)
n = int(input("Enter the number of elements (n): "))

# Step 2: Initialize an empty list to act as our array
array_stor = []

# Step 3: Loop 'n' times to read inputs from the user
print(f"Please enter your {n} elements:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    array_stor.append(element)  # Store it in the array

# Step 4: Loop through the array and print the elements
print("\nThe elements stored in the array are:")
for items in array_stor:
    print(items)

