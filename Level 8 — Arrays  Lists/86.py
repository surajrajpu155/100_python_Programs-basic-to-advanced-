# 86. Write a program to find the second largest element in an array.

array_element = [59, 57, 56, 75, 89]

un_set = set(array_element)
un_list = list(un_set)

second_largest = sorted(un_list)[-2]
print(second_largest)

# second_larges = sorted(list(set(array_element)))[-2]  # one line code