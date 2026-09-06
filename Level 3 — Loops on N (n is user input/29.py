# 29. Write a program to display the multiplication table of a number n.

n = int(input("Enter a number want to print multiplication table  : "))
print(f"multiplication table of {n}")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    
