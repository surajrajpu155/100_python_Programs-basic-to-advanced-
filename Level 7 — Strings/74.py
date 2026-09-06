# 74. Write a program to count the frequency of each character in a string.

text = "suraj kumar singh"

dict_stor = {}

for ch in text.lower():
    
    # dict_stor = text.count(ch)
    if ch not in dict_stor:
        dict_stor[ch] = 1
    
    else:
        dict_stor[ch] += 1

for ch, count in dict_stor.items(): # print items from dict
    print(f"'{ch}' : {count}")
    
