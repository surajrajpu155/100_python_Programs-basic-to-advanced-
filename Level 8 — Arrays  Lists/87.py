# 87. Write a program to count the frequency of each element in an array.

text_list = [20,45, 45, 65, 65, 89, 89] 
dict_stor = {}

for i in text_list:
    if i not in dict_stor:
        dict_stor[i] = 1
    
    else:
        dict_stor[i] += 1

for ch, count in dict_stor.items(): # print items from dict
    print(f"'{ch}' : {count}")
    
