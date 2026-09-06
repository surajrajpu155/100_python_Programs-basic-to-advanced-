# 31. Write a program to count how many numbers from 1 to n are divisible by 3.

n = int(input("Enter a number to check how many numbers up to it are divisible by 3: "))

count = 0

for i in range(1, n+1):
    if i % 3 == 0:
        print(i)
        count = count + 1
print(f"Total numbers divisible by 3 from 1 to {n} = {count}")
