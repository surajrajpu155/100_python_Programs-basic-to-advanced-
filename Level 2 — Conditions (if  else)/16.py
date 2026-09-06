# 16. Write a program to read a character and check whether it is a vowel or a consonant.

s = input("Enter a single character : ")
vol = "a", "A", "e", "E", "i", "I", "o", "O", "u", "U" 

while True:
    if s == vol[0]:
        print(f"{s}' is a vowel.")
    elif s == vol[1]:
        print(f"{s}' is a vowel.")
    elif s == vol[2]:
        print(f"{s}' is a vowel.")
    elif s == vol[3]:
        print(f"{s}' is a vowel.")
    elif s == vol[4]:
        print(f"{s}' is a vowel.")     
    else:
        print(f"{s}' not a vowel")
    break