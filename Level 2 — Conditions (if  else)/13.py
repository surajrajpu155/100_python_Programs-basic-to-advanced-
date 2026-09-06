# 13. Write a program to read three numbers and find the largest among them.

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))


if num1 > num2 and num1 >num3:
    print(f"num {num1} is largest ")
elif num2 > num3:
    print(f"{num2} is largest  ")
else:
    print(f"{num3} is largest ")
