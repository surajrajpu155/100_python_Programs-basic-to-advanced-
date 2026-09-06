# 9. Write a program to read the marks of 5 subjects and print the total and average.

English = int(input("Enter your marks in English : "))
Hindi = int(input("Enter your marks in Hindi : "))
Physics = int(input("Enter your marks in Physics : "))
Chemistry = int(input("Enter your marks in Chemistry : "))
Mathematics = int(input("Enter your marks in Math : "))

total = English + Hindi + Physics + Chemistry + Mathematics
avarage = total / 5

print(f"You have got {total} marks out of 500.")
print(f"Your average mark is {avarage} marks")