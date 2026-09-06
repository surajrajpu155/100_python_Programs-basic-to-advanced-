# 35. Write a program to find the sum of all digits of a number n.

n = 123
sum = 0

while n > 0:
    r = n % 10
    sum =sum + r
    n //= 10  
    
print(sum)   