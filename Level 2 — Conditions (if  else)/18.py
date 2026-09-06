# 18. Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).

marks = int(input("Inter you marks lessthan 100 : "))

if marks >= 90:
    print("A grade")
    
elif marks >= 70:
    print("B grade ")
    
elif marks >= 60:
    print("C grad")
    
elif marks >= 33:
    print("D grade")

elif marks in range(0, 33):
    print("Fail")
    
else:
    print("Invalad input !")