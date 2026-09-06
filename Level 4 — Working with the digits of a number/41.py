# 41. Write a program to check whether a number n is a palindrome (reads the same reversed).

n = 121

orignal_number = n 
reverse_number = 0

while n > 0:
    last_dig = n % 10 
    reverse_number = reverse_number * 10 + last_dig
    
    n //= 10
    
if reverse_number == orignal_number: 
    print("your nnumber is palindrome ")

else :
    print("not palindrom")