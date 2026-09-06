# 22. Write a program to display all natural numbers from 1 to n in reverse order.

n = int(input("Enter a number : "))
print(f"Natural numbers from {n} to 1 ")

for i in range(n, 0, -1):
    print(i)
    