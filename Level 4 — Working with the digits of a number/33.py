# 33. Write a program to count the number of digits in a number n.

n = 3545
count = 0

# for i in n:   # using n as a string than work it
#     print(i)

if n == 0:
    count += 1
else:
    while n > 0:
        n //=  10
        count += 1
        
print(count)
