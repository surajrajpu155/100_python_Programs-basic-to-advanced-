# 88. Write a program to remove duplicate elements from an array.

text_list = [20, 45, 45, 65, 65, 89, 89] 

removed = list(set(text_list))
print(removed)


list(dict.fromkeys(text_list))