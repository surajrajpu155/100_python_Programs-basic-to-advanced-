# 47. Write a program to check whether a number is an Armstrong number.

n = int(input("Enter a number to check armstrong or not : "))
orignal_number = n
dig_count = 0
sum = 0

while (n > 0): # for check digits in number
    dig_count += 1
    n //= 10
    
n = orignal_number

while (n > 0):
    last_d = n % 10
    sum += last_d ** dig_count
    
    n //= 10
    
if sum == orignal_number:
    print(f"{orignal_number} is A Armstrong number! ")
else:
    print("Not Armstrong ")
        