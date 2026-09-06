# 27. Write a program to find the sum of all odd numbers from 1 to n.

n = int(input("Enter a number : "))
print(f"all odd numbers from 1 to {n}")
sum = 0

for i in range(1, n):
    if i % 2 != 0:
        sum = sum + i
        
print(sum)
