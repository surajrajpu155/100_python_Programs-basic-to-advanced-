# 43. Write a program to find the sum of the first and last digit of a number n.

n = 1234
last_dig = 0

last_dig = n % 10

while n > 10:
    n //= 10
    
first_dig = n

sum_dig = first_dig + last_dig
print(f"sum of first_dig and last_dig = {sum_dig}")