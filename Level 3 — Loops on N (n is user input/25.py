# 25. Write a program to find the sum of all natural numbers from 1 to n.

n = int(input("Enter a number : "))
print(f"sum of all natural numbers from 1 to {n}")

sum = 0
for i in range(1, n+1):
    sum = i + sum
print(sum)