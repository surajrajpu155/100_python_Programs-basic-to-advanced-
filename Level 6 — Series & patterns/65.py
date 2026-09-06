# 65. Write a program to print a pyramid pattern of stars of height n.

n = int(input("Enter the height of pyramid: "))

for i in range(1, n + 1):
    # Print (n - i) spaces, then concatenate with i stars followed by spaces
    print(" " * (n - i) + "* " * i)
