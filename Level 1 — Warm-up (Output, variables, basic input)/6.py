# 6. Write a program to swap two numbers using a third variable.

a = int(input("enter first number = "))
b = int(input("enter secodn number = "))

c = a + b

a = c - a
b = c - b
print(f"swap a = {a}")
print(f"swap b = {b}")