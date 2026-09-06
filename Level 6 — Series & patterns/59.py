# 59 Write a program to find the sum of the series 1 + 2 + 3 + ... + n.

n = int(input("Enter a number : "))

sum = 0
for i in range(1, n+1):
    print(i)
    sum += i
print(f"Sum of the number = {sum}")