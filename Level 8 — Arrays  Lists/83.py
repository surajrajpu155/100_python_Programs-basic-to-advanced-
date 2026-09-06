# 83. Write a program to count the number of even and odd elements in an array.

array_element = [59, 57, 56, 75, 89]
even_count = 0
odd_count = 0

for i in array_element:
    if i % 2 ==0:
        even_count += 1
    else:
        odd_count += 1

print(f"number of even number in {array_element} is : {even_count}")
print(f"number of odd number in {array_element} is : {odd_count}")