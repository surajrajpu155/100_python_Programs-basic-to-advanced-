# 30. Write a program to display all multiples of a number m up to n terms.

m = int(input("Enter a number want to print table  : "))
n = int(input("Enter a number want to print last term : "))

for i in range(1, n+1):
    print(f"{m} * {i} = ", m*i)

