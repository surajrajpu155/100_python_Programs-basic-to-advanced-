# 76. Write a program to check whether two strings are anagrams of each other.

str1 = "Sisten"
str2 = "Silent"

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Yes, they are Anagrams!")
else:
    print("No, they are not Anagrams.")
