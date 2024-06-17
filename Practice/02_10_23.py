# # [1,1,1,2,4,8,3,9,27,4,16,64]
# print([i ** j for i in range(1, 5) for j in range(1, 4)])

# str1 = "Testing python programming Language" 
# # Output {'o': x, 'i': x, 'a': x, 'e': x, 'u': x}

# str_new = (str1.replace(" ", "")).lower()
# print(str_new)

# vowels = ['a', 'e', 'i', 'o', 'u']
# dict1 = {}

# for i in str_new:
#     if i in vowels:
#         if i in dict1:
#             dict1[i] = dict1[i] + 1
#         else:
#             dict1[i] = 1
            
# print(dict1)

# COUNT NUMBER OF EVEN AND ODD

# def count_odd_even(list1):
#     a = 0
#     b = 0
    
#     for i in list1:
#         if i % 2 == 0:
#             a += 1
#         else:
#             b += 1 
#     return a, b

# list1 = [1, 3, 4, 2, 6, 77, 87, 90, 99]

# a, b = count_odd_even(list1)
# print(f"Even is {a} and Odd is {b}")

# FIBONACCI
# [0, 1, 1, 2, 3, 5, 8, 13, ....]

# def fibonacci(num):
#     a = 0
#     b = 1
    
#     if num <= 0 :
#         print("Fibonacci Not Possible")
#     elif num == 0:
#         return num
#     else:
#         print(a, end = " ")
#         print(b, end = " ")
        
#         for i in range(num):
#             c = a + b
#             a = b
#             b = c
#             print(c, end = " ")    

# num = int(input("Enter the limit of Fibonacci : "))
# fibonacci(num)

# FACTORIAL 
# 5 x 4 x 3 x 2 x 1 = 120

# def factorial(num):
#     f = 1
#     for i in range(1,num + 1):
#         f = f * i 
#     return f
       
# print(factorial(5))

#Printing Uncommon from both the lists

# list1 = ["apple","orange","banana"]
# list2 = ["orange","apple","grapes"]
# uncommon = []

# for i in list1:
#     if i not in list2:
#         uncommon.append(i)
# print(uncommon)

# Print Bigrams

# str1 = "Ram is a good boy"
# str2 = str1.split()
# list2 = []

# for i in range(len(str2) - 1):
#     list1 = str2[i], str2[i + 1]
#     list3 = tuple(list1)
#     list2.append(list1)
# print(list2)
       
# ARMSTRONG NUMBER
# 153 = (1 X 1 X 1)+(5 X 5 X 5)+(3 X 3 X 3)

# number = int(input("Enter a number : "))
# sum = 0

# temp = number

# while temp > 0:
#     digit = temp % 10
#     cube = digit ** 3
#     sum = sum + cube
#     temp = temp // 10
    
# if sum == number:
#     print("It's an Armstrong number")
# else:
#     print("It's not an Armstrong number")

# NUMBER PALINDROME
# 123 ----> 321

# def reversed_num(number):
#     reverse_num = 0
    
#     while number > 0:
#         obtained_first = number % 10
#         reverse_num = reverse_num * 10 + obtained_first
#         number = number // 10
#     return reverse_num

# num = int(input("Enter the number you want to reverse : "))
# print(reversed_num(num))

# Words Palindrome

# word = input("Enter a word : ")
# rev_word = word[::-1]

# if rev_word == word:
#     print("Yes! It's a Palindrome")
# else:
#     print("No! It's not a Palindrome")

print("a" * 4)
print(4 * "a")

