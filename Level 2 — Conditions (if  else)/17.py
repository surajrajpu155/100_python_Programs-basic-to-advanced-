# 17. Write a program to read a character and check whether it is an alphabet, digit or special symbol.

user = input("Enter a single (alphabet, digit or special symbol ) = ")

if user.isalpha():
    print(f"{user}' is a alphabet !")
elif user.isdigit():
    print(f"{user}' is a digit")
else:
    print(f"{user}' is a Special Symbol")