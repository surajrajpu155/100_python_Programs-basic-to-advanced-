# 45. Write a program to display all prime numbers from 1 to n.

n = int(input("enter a number to print prime : "))
primes = []

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            primes.append(num)
print(primes)
