# 48. Write a program to display all Armstrong numbers from 1 to n.

n = int(input("Enter the limit n: "))

print(f"Armstrong numbers from 1 to {n}:")

for num in range(1, n + 1):
    # Store the number in temporary variables
    temp1 = num
    temp2 = num
    
    # Step 1: Count the total number of digits
    dig_count = 0
    while temp1 > 0:
        dig_count += 1
        temp1 //= 10
        
    # Step 2: Calculate the sum of digits raised to the power of dig_count
    total_sum = 0
    while temp2 > 0:
        last_digit = temp2 % 10
        total_sum += last_digit ** dig_count
        temp2 //= 10
        
    # Step 3: Print the number if it matches the original sum
    if total_sum == num:
        print(num, end=" ")
