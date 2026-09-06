# 66. Write a program to print a number triangle (row i contains numbers 1 to i).

n = 6
for j in range(1, n):
    
        print(" " * (n - j) + "* " * j)
    