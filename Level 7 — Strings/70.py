# 70. Write a program to count the number of words in a sentence.

name = "suraj kumar singh"
count = 0
for ch in name:
    if ch.isalpha():
        count += 1
print(count)
