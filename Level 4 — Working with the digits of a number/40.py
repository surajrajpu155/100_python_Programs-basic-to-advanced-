# 40. Write a program to count the number of even digits and odd digits in a number n.

n = 5679
print(f"your number is = {n}")
even = 0
odd = 0

while n > 0:
    last_dig = n % 10 
    
    if last_dig % 2 == 0:
        even += 1
    else:  # we can use  elif last_dig % 2 != 0
        odd += 1 
    
    n //= 10


print(f"number of even is = {even}")
print(f"number of odd is = {odd}")