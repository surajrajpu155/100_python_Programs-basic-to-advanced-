# 84. Write a program to search for an element in an array (linear search).

array_element = [59, 57, 56, 75, 89]

target = 75

for i in array_element:
    if i == target:
        print(f"{target} found successfully! at index : ", array_element.index(i))
        break
else:
    print(f"{target} not found!")