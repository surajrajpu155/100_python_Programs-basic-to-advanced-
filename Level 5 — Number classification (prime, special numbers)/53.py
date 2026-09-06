# 53. Write a program to find all factors (divisors) of a number n.

n = int(input("Enter a number to find all factors : "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)