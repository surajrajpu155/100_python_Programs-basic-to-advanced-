# 92. Write a program to check whether a number is prime, using a function/method.

# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             print("your number is not prime ")
#             break
#     else:
#         print("number is prime")
            
# check_prime(9)



def prime(n):
    if n <= 1:
        return "Not prime"
    sqr = n ** 0.5
    
    if sqr.is_integer():
        return "prime"
    limit = int(sqr)  # Yeh decimals ko hata kar '2' kar dega
    for i in range(2, limit + 1):
        if n % i == 0:
            return "Not prime"

    return "prime"

print(prime(5))