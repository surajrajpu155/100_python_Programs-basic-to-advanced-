# 14. Write a program to read three numbers and find the smallest among them.

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))

if num1 < num2 and num1 < num3:
    print(f"{num1} is smallest ")
    
elif num2 < num3:
    print(f"{num2} is smallest ")
    
else:
    print(f"{num3 } is smallest")