# 19. Write a program to read a number and check whether it is divisible by both 3 and 5.

number = int(input("Enter number to check it is divisible by both 3 and 5 : "))

sum = sum(int(digit) for digit in str(number)) 
div_3 = sum % 3 == 0

div_5 = number % 5 == 0

if div_3 and div_5:
    print(f"{number} is divisible by both 3 and 5. ")


