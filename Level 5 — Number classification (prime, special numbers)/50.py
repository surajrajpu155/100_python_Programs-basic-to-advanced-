# 50. Write a program to check whether a number is a strong number (sum of factorials of its digits).


n = int(input("Enter a number to check whether a number is a strong number : "))
temp1 = n

sum = 0

while (n > 0):
    fact = 1
    last_dig = n % 10
    for i in range(1, last_dig + 1):
        fact *= i
    sum += fact

    n //= 10

print(sum)
if temp1 == sum:
    print(f"{temp1} is a strong number  !")
else:
    print(f"{temp1} is not a strong number ")
