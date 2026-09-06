# 79. Write a program to toggle the case of each character in a string.

text = "Suraj"
result = ""

for ch in text:
    if 'a' <= ch <= 'z':
        result += ch.upper()  # Convert small to capital
    elif 'A' <= ch <= 'Z':
        result += ch.lower()  # Convert capital to small
    else:
        result += ch          # Keep spaces or numbers unchanged

print(result)  # Output: sURAJ


text = "Suraj Kumar"
toggled_text = text.swapcase()

print(toggled_text)  # Output: sURAJ kUMAR
