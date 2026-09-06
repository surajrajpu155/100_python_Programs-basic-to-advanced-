# 36. Write a program to find the product of all digits of a number n.

n = 1235
pro = 1

while n > 0:
    r = n % 10
    pro =pro * r
    n //= 10  
    
print(pro)   