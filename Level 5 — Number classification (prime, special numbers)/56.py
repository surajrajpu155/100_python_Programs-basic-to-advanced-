# 56. Write a program to find the LCM of two numbers.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))


# 1. Save original values because num1 and num2 will change in the loop
a = num1
b = num2

while num2 != 0:
    num1, num2 = num2, num1 %  num2
hcf = num1

lcm = (a * b) / hcf
print("lcm = ",lcm)