# 60. Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.


n = int(input("Enter a number : "))

sum = 0

for i in range(1, n+1):
    print(i**2)
    sum += i**2
print(f"Sum of the number = {sum}")