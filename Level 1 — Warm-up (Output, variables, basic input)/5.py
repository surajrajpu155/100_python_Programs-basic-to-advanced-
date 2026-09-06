# 5. Write a program to read the length and breadth of a rectangle and print its area and perimeter.


l = int(input("Enter length of rectangle : "))
b = int(input("Enter breadth of rectangle : "))

area = l * b 
p  = 2*(l + b)

print(f"Area is {area}")
print(f"perimeter is {p} " )
