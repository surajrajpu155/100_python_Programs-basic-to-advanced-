# 39. Write a program to find the smallest digit in a number n.
n = 436
smallest = 9

while n > 0 :
    last_dig = n % 10 
    
    if last_dig < smallest:
        smallest = last_dig
        
    n //= 10

print(smallest)