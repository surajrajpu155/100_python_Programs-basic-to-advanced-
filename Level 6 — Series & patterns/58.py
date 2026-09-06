# 58. Write a program to find the sum of the first n terms of the Fibonacci series.

n = int(input("Enter the number of terms: "))
fib_sum = 0 
a ,b = 0, 1


for i in range(0, n):
    print(f"{a} ", end=",")
    fib_sum += a
    a, b = b, a +b

print(f"\nsum of the first {n} terms of the Fibonacci serie : {fib_sum}")