# 42. Write a program to replace all zeros in a number n with the digit 5.

n = 14050
replace_value = 0 

while n > 0:
    last_dig = n % 10 
    
    if last_dig == 0:
        last_dig = 5
    
    replace_value = replace_value * 10 + last_dig
    
    n //= 10
    

orignal_number = 0  
while replace_value > 0:
    last_di = replace_value % 10
    orignal_number = orignal_number * 10 + last_di
    
    replace_value //= 10
        
print(orignal_number)