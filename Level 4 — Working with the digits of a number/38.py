# 38. Write a program to find the largest digit in a number n.

n =  5839

largest = 0

while n > 0:
    last_dig = n % 10
    
    if last_dig > largest:
        largest = last_dig
        
    n //= 10 
    

print(largest)