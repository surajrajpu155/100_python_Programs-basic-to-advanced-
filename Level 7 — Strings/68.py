# 68. Write a program to find the length of a string without using an inbuilt function.

name = "suraj kumar singh"
count = 0

for i in name:
    if i.isalpha():
        count += 1
print(count)