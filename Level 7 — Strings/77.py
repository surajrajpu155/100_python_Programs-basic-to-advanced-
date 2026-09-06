# 77. Write a program to find the first non-repeating character in a string.


text = "sw  `A=i  0987652wq1ss"
# text = "racecar"

dict_stor = {}

for ch in text.lower():
    
    # dict_stor = text.count(ch)
    if ch not in dict_stor:
        dict_stor[ch] = 1
    
    else:
        dict_stor[ch] += 1
print(dict_stor)
found = False
for ch, count in dict_stor.items():
    if count == 1:
        print(f"First non-repeating character: {ch}")
        found = True
        break  # 💡 This stops the loop immediately!

if not found:
    print(f"No non-repeating character found in: {text}")