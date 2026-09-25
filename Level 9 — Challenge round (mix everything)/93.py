# 93. Write a program to print all prime numbers between two given numbers a and b.


a = int(input("enter starting point : "))
b = int(input("Enter ending point : "))

def prime(n):
    if n <= 1:
        return False

    limit = int(n ** 0.5)

    for i in range(2, limit + 1):
        if n % i == 0:
            return False

    return True

def print_primes(a, b):
    for n in range(a, b + 1):
        if prime(n):
            print(n, end=", ")

print_primes(a, b)