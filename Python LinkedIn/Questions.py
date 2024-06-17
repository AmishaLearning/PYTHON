# Factors

# factors =[]

# def factorss(num):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)
            
# num = int(input("Enter the number to find its prime factors :"))
# factorss(num)
# print(factors)

# Prime Factors

# def get_prime_factors(number):
#     factors = []
#     divisor = 2
    
#     while divisor <= number:
#         if number % divisor == 0:
#             factors.append(divisor)
#             number = number // divisor # Gives Quotient
#         else:
#             divisor += 1
#     return factors

# number = int(input("Enter the number to find its prime factors : "))
# print(get_prime_factors(number))

# Palindrome

# def is_palindrome(value):
#     value = value.lower()
#     for i in value:
#         if not i.isalpha():
#             value = value.replace(i, "")   
        
#     if value == value[::-1]:
#         return True
#     else:
#         return False
   
# value = input("Enter a string of your choice : ")
# print(is_palindrome(value))

# Sort Strings

# def input_strings(string):
#     string_list = string.split()
#     sorted_strings = sorted(string_list, key = lambda x : x.lower())
#     return " ".join(sorted_strings)
        
# string = input("Enter a String : ")
# print(input_strings(string))

# Find all list items

# def index_all(search_list, item):
#     index_list = []
#     for index, value in enumerate(search_list):
#         if value == item:
#             index_list.append([index])
#         elif isinstance(value, list):
#             for i in index_all(value, item):
#                 index_list.append([index] + i)
#     return index_list

# my_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# result = index_all(my_list, [1,2,3])
# print(result)

# Waiting Game

# import time
# import random

# def waiting_game():
#     target = random.randint(2, 4)
#     print(f"Your Target time is {target} seconds..")
    
#     input("----Press Enter To Begin----")
#     start = time.perf_counter()
#     input(f"--Press Enter again after {target} seconds--")
#     elapsed = time.perf_counter() - start
    
#     print(f"Elasped time : {elapsed :.3f} seconds")
#     if elapsed == target:
#         print("Unbelieveable! Perfect Timing!!")
#     elif elapsed < target:
#         print(f"({target - elapsed :.3f} seconds Too Fast)")
#     else:
#         print(f"({elapsed - target :.3f} seconds Too Fast)")
        
# waiting_game()
        

    