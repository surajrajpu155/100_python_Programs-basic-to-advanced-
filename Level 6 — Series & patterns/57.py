# 57. Write a program to display the first n terms of the Fibonacci series.

n = int(input("Enter the number of terms: "))

a ,b = 0, 1


for i in range(0, n):
    print(f"{a} ", end=" ")
    a, b = b, a +b
    