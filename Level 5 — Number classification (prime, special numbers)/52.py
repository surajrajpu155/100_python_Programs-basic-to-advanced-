# 52. Write a program to check whether a number is a Harshad (Niven) number.

n = int(input("Enter a nummber to check whether a number is a Harshad (Niven) number = "))
temp = n
sum = 0

while n > 0:
    last_dig = n % 10
    sum += last_dig
    
    n //= 10
    
if sum > 0 and temp % sum == 0:
    print(f"{temp} is a Harshad number ")
else:
    print(f"{temp} is not a Harshad number ")
    
    