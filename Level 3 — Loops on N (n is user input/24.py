# 24. Write a program to display all odd numbers from 1 to n.

n = int(input("Enter a number : "))
print(f"all odd numbers from 1 to {n}")

for i in range(1, n):
    if i % 2 != 0:
        print(i)
