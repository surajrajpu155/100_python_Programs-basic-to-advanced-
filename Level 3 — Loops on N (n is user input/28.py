# 28. Write a program to find the product of all natural numbers from 1 to n (factorial of n).


n = int(input("Enter a number : "))
print(f"product of all natural numbers from 1 to {n}")

pro = 1
for i in range(1, n+1):
    pro = pro * i

print(pro)    