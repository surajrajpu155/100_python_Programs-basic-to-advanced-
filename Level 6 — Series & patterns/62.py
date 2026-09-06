# 62. Write a program to find the value of x raised to the power y without using inbuilt power.

x = int(input("Enter a x value : "))
y = int(input("Enter a y value : "))

sqrt = x
if y ==0:
    print("1")
else:
    for i in range(1, y):
    
        sqrt *= x
    print(sqrt)