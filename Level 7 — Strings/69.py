# 69. Write a program to count the number of vowels and consonants in a string.

name = "suraj kumar singh"
vow = 0
con = 0

vowels =  "aeiou"

while True:
    for ch in name:
        if ch == "a" or ch == "A":
            vow += 1
        elif ch == "e" or ch == "E" :
            vow += 1
        elif ch == "i" or ch == "I" :
            vow += 1
        elif ch == "o" or ch == "O" :
            vow += 1
        elif ch == "u" or ch == "U" :
            vow += 1
        elif ch.isalpha():
            con += 1
    break
print("vowels is : ",vow)
print("consonants is :", con)