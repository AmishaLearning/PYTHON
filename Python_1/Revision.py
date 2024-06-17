#FACTORIAL

# def factorial(x):
#     f = 1
#     for i in range(1, num + 1):
#         f = f * i 
#     print(f)

# num = int(input("Enter the number who's factorial you require : "))
# factorial(num)

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# n = int(input("Enter the number who's factorial you require : "))
# print(fact(n))
    
    
#FIBONACCI SERIES
# 0 1 1 2 3 5 8 13 21 34....

# def fibo(n):
#     a = 0
#     b = 1
#     if n < 1:  
#         print("Fibonacci Series not possible")
#     elif n == 1:
#         print(a)
#     else:
#         print(a, end=" ")
#         print(b, end=" ")
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c        
#             print(c, end=" ")
        
# n = int(input("Enter the number till which you want the series : "))
# fibo(n)
        
#ARMSTRONG NUMBER
# 153 = (1x1x1) + (5x5x5) + (3x3x3) = 153

# number = int(input("Enter a number : "))
# sum = 0
# temp = number

# while temp > 0:
#     digit = temp % 10
#     print(digit)
#     cube = digit ** 3
#     print(cube)
#     sum = sum + cube
#     print(sum)
#     temp = temp // 10
#     print(temp)

# if sum == number:
#     print("Yes!! It's an Armstrong Number")
# else:
#     print("No!!It's not an Armstrong Number")

#PALINDROME NUMBER

def reverse_num(num1):
    reversed_num = 0
    
    while num1 > 0:
        first = num1 % 10
        reversed_num = reversed_num * 10 + first
        num1 = num1 // 10
        
    return reversed_num
number_reverse = int(input("Enter the number to obtain reverse : "))
print(reverse_num(number_reverse))
    