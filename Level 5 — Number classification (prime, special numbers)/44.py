# 44. Write a program to read a number and check whether it is prime or not.

n = int(input("enter a number : "))
count = 0

if n == 1 :
    print("not prime")
    
    
else:
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
            if count >= 2:
                break
            
    if count < 2:
        print("prime numbe")
    else:
        print("not prime")
            
        