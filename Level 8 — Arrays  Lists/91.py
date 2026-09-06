# 91. Write a program to find the sum of all even-indexed and odd-indexed elements separately.

array_element = [10, 20, 30, 40, 50, 60]

even_index_sum = 0
odd_index_sum = 0

for i in range(len(array_element)):
    if i % 2 == 0:
        even_index_sum += array_element[i]
    
    elif i % 2 != 0:
        odd_index_sum += array_element[i]

print(f"Even-indexed sum: {even_index_sum}")
print(f"Odd-indexed sum: {odd_index_sum}")