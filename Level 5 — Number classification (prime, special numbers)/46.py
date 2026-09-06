# 46. Write a program to display the first n prime numbers.

num = 10

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break
        
else:
    print("prime")