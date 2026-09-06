# 51. Write a program to check whether a number is an automorphic number.

n = int(input("Enter a number to check whether a number is an automorphic number : "))
temp1 = n
square = n ** 2

while n > 0 :
    last_dig = n % 10
    sq_last_dig = square % 10  # Aapke square ka aakhiri digit
    
    # Agar dono ke aakhiri digits match nahi huye, toh loop break ho jayega
    if last_dig != sq_last_dig:
        break
    
    n //= 10
    square //= 10  # Sq
if last_dig == sq_last_dig :
    print(f"{temp1} is a automorphic number.")
else:
    print(f"{temp1} is not a automorphic number.")
    
    
    
