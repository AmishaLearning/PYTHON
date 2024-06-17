# LEET CODE
# TWO SUM

# list1 = [2, 5, 6, 3, 8, 9, 10]
# target = 11

# for i, num1 in enumerate(list1):
#     for j, num2 in enumerate(list1[i + 1: ]):
#         if num1 + num2 == target:
#             print(f"Yes! Target is obtained at index : {i} and {i + j + 1}")

# list1 = [1, 2, 3, 4, 5, 6]
# target = 8

# for item_1 in list1:
#     # print(item_1)
#     for item_2 in list1:
#         number = item_1 + item_2   
#         if number == target:
#             print("item 1 :", item_1, "item 2 : ", item_2)
#             print("Yes")    
#             break


# ADD TWO NUMBERS

# list1 = [2, 4, 3]
# list2 = [5, 6, 4]

# result_1 = 0
# result_2 = 0

# list1.reverse()
# list2.reverse()

# for digit_1 in list1:
#     result_1 = result_1 * 10 + digit_1

# for digit_2 in list2:
#     result_2 = result_2 * 10  + digit_2
    
# final_sum = result_1 + result_2
# final_list = []

# while final_sum > 0:
#     final_list.append(final_sum % 10)
#     final_sum = final_sum // 10
#     # digit_1 = final_sum % 10
#     # final_list.append(digit_1)

#     # number = final_sum // 10
#     # digit_2 = number % 10
#     # final_list.append(digit_2)

#     # number_1 = number // 10
#     # digit_3 = number_1 % 10
#     # final_list.append(digit_3)

# print(final_list)

# Write a program to print the given number is odd or even.

# number = int(input("Enter a number : "))

# if number % 2 == 0:
#     print("The number is Even")
# else:
#     print("The number is Odd")

# Write a program to find the given number is positive or negative.

# number = float(input("Enter a number : "))
# if number > 0:
#     print("The number is Positive")
# elif number == 0:
#     print("The number Zero")
# else:
#     print("The number is Positive")

# Write a program to find the sum of two numbers.

# num1 = float(input("Enter the First number  : "))
# num2 = float(input("Enter the Second number : "))

# print(f"The sum of {num1} and {num2} is : {num1 + num2}")

# Write a program to find if the given number is prime or not.

# number = int(input("Enter a number : "))
# count = 0
# for i in range(2 , number + 1):
#     if number % i == 0:
#         count += 1
   
# if count > 1:
#     print(f"The given number {number} is Not Prime")
# else:
#     print(f"The given number {number} is Prime")

# Write a program to check if the given number is palindrome or not.

# num = int(input("Enter a number : "))
# temp = num
# reverse_num = 0

# while temp > 0 : 
#     obtained_first = temp % 10
#     reverse_num = (reverse_num * 10) + obtained_first
#     temp = temp // 10

# if num == reverse_num:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# Write a program to check if the given number is Armstrong or not

# num = int(input("Enter a number : "))
# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     cube = digit ** 3
#     sum = sum + cube
#     temp = temp // 10

# if sum == num:
#     print("Yes! It's an Armstrong Number")
# else:
#     print("No! It's Not an Armstrong Number")

# Write a program to check if the given strings are anagram or not

# def check(s1, s2):
#     if sorted(s1)== sorted(s2):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")

# s1 = input("Enter S1 : ")
# s2 = input("Enter S2 : ")
# check(s1, s2)

# Write a program to find a factorial of a number.

# num = int(input("Enter the numbers whose factorial u want to find : "))
# f = 1
# for i in range(1, num + 1):
#     f = f * i
# print(f)

# Write a program to find a fibonacci of a number.

# def fibonacci(num):
#     if num <= 0 :
#         print("Fibonacci Not Possible")
#     elif num == 1:
#         return num
#     else:
#         a = 0
#         b = 1
#         print(a, end = " ")
#         print(b, end = " ")
        
#         for i in range(2, num):
#             c = a + b
#             a = b
#             b = c
#             print(c, end = " ")
# num = int(input("Enter the number of terms in fibonacci series : "))
# fibonacci(num)

# Pattern 
# n = 5
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("*", end = " ")
#     print("\r")

# Display Multiplication table using loop

# num = int(input("Enter a number : "))

# for i in range(1, 11):
#     print(num ,"X", i, "=", num * i)

