# 73. Write a program to convert a string to uppercase and lowercase without inbuilt case functions.

# print(ord("A")) # 65
# print(ord("Z")) # 90 upper_case = 65 to 90
# print(ord("a")) #97
# print(ord("z")) #122 lower_case = 97 to 122
# print(chr(97))
# print(chr(ord("a") -32))

text = "Suraj Kumar Singh"
upper_text = ""
lower_text = ""

for ch in text:
    asc = ord(ch)
    if asc >= 65 and asc <= 90:
       upper_text = upper_text + chr(asc + 32)
    else:
        upper_text = upper_text + chr(asc)
        
    if asc >= 97 and asc <= 122:  # we can use range(97, 123) function but the range function takes more time to check 
        lower_text = lower_text + chr(asc -32)      
    else:
        lower_text = lower_text + chr(asc)
        
        
print(upper_text)
print(lower_text)