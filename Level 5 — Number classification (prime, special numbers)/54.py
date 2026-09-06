# 54. Write a program to count the number of factors of a number n.

n = int(input("Enter a number to find all factors : "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1
print(count)