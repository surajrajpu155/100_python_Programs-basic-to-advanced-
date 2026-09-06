# 61. Write a program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n.


n = int(input("Enter a number : "))

sum = 0

for i in range(1, n+1):
    sum += 1/i
print(sum)