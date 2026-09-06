# 72. Write a program to check whether a string is a palindrome.
# NITIN ➡️ NITIN MADAM➡️MADAM RADAR➡️RADAR

# convert user input to lowercase
text = input("Enter a word: ").lower()

reversed_text = text[::-1]


if text == reversed_text:
    print("Yes, it is a Palindrome!")
else:
    print("No, it is not a Palindrome.")
