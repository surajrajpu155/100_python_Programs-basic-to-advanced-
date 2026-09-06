# 49. Write a program to check whether a number is a perfect number.

n = int(input("Enter a number to perfect or not : "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if n == sum:
    print(f"{n} is a perfact number !")
else:
    print(f"{n} is not a perfect number")