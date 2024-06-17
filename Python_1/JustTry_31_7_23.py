# #Method Overriding
# class A:
#     def sum():
#         sum = (5 + 6)/2
#         print("From class A")
#         return sum
    
# class B(A):
#     def sum():
#         sum = (10 + 10)/5
#         print("From class B")
#         return sum
    
# print(B.sum())

# #Method Overloading

# class C:
#     def subtract():
#         sub = (20 - 10)/2
#         print("From class C part 1")
#         return sub
    
#     def subtract():
#         sub = (40 - 10)/2
#         print("From class C part 2")
#         return sub
        
# print(C.subtract())

# list1 = [1,2,3,4,5,1,1,2,3,1,1,1,1]
# x = 1
# count = 0
# for i in list1:
#     if i == x:
#         count = count + 1
        
# print("The count is : ",count)

# def fact(x):
#     if (x == 0 or x == 1):
#         return 1
#     else:
#         return x * fact(x-1)

# n = int(input("Enter the number : "))
# print(fact(n))

# def fact(n):
#     return 1 if (n == 0 or n == 1) else n * fact(n-1)
# num = int(input("Number : "))
# print("The factorial is : ",fact(num))

# def fibo(n):
#     a = 0
#     if n <= 0:
#         print("Not possible")
        
#     elif n == 1:
#         print(a = 0)
#     else:
#         b = 1
#         print(a , end=" ")
#         print(b ,end=" ")
#         for i in range(2, n):
#             c = a + b
#             a = b 
#             b = c
#             print(c, end=" ")
            
# num = int(input("enter number : "))
# fibo(num)

#[1,1,1,2,4,8,3,9,27,4,16,64]
# print([i ** j for i in range(1,5) for j in range(1,4)])

# Number palindrome
# def reversed(number):
#     reverse_num = 0
    
#     while number > 0:
#         obtained_num = number % 10
#         reverse_num = reverse_num * 10 + obtained_num
#         number = number // 10
    
#     return reverse_num

# num = int(input("enter the number : "))
# print(reversed(num))

#ARMSTRONG
# number = int(input("Enter number : "))
# sum = 0
# temp = number

# while temp > 0:
#     digit = temp % 10
#     cube = digit ** 3
#     sum = sum + cube
#     temp = temp // 10
    
# if sum == number:
#     print("Yes")
# else: 
#     print("No")

# str1 = "Geeks for geeks"
# str2 = str1.replace(" ","")
# print(str2)

# vowels = ['a','e','i','o','u']

# dict1 ={}

# for i in str2:
#     if i in vowels:
#         if i in dict1:
#             dict1[i] = dict1[i] + 1
#         else:
#             dict1[i] = 1

# print(dict1)
       
#FACTORIAL
# num = int(input("Enter the number : "))
# f = 1
# for i in range(1, num + 1):
#     f = f*i
    
# print("The factorial is : ",f)