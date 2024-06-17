#Factorial

# def fact(n):
#     f = 1
#     for i in range(1,  n + 1):
#         f = f * i
#     return f
# n = int(input("Enter a number : "))
# print(fact(n))
    
# def fact(num):
#     if num == 0:
#         return 1
#     return num * fact(num - 1)
# num = int(input("Enter a number : "))
# print(fact(num))

#Fibonacci

# def fibo(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n < 1:
#         print("Not possible")
#     else:
#         print(a, end = " ")
#         print(b, end = " ")
#         for i in range(1, n + 1):
#             c = a + b
#             a = b
#             b = c
#             print(c, end = " ")
# n = int(input("Enter till where you want the fibonacci series : "))
# fibo(n)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter a number : "))

# if n <= 1:
#     print("Enter a positive number. ")
    
# else:
#     for i in range(n):
#         print(fibonacci(i), end = " ")

# #Number Palindrome

# def reverse(number):
#     reverse_num = 0
    
#     while number > 0:
#         obtained_first = number % 10
#         reverse_num = reverse_num * 10 + obtained_first
#         number = number // 10
#     return reverse_num

# num = int(input("Enter the number : "))
# print(reverse(num))

#ARMSTRONG
# 153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3* 3) = 153

# number = int(input("Enter a number : "))
# sum = 0
# temp = number

# while temp > 0:
#     digit = temp % 10
#     cube = digit ** 3
#     sum = sum + cube
#     temp = temp // 10
    
# if sum == number:
#     print("Yes !! Armstrong")
# else:
#     print("No !!Not an Armstrong")

a = {1, 2, 3, 1}
print(type(a))