# Are two Strings equal
# 1

# def equal(first_string, second_string):
#     if first_string == second_string:
#         return True
#     else:
#         return False

# first_string = input("Enter the First String : ")
# second_string = input("Enter the second String : ")    
# print(equal(first_string, second_string))

# 2

# def check_strings(first_string, second_string):
#     return first_string == second_string

# first_string = input("Enter the First String : ")
# second_string = input("Enter the second String : ")    
# print(check_strings(first_string, second_string))

# STRING REPLACEMENT

# def replace_string(orig_string, old_string, new_string):     
#     if old_string in orig_string:
#         modified_string = orig_string.replace(old_string, new_string)
#         return modified_string
#     else:
#         return orig_string

# orig_string = input("Enter the Original String : ")
# old_string = input("Enter the Old String : ")
# new_string = input("Enter the New String : ")          
# print(replace_string(orig_string, old_string, new_string))

# def replace_string(orig_string, old_string, new_string):     
#     return orig_string.replace(old_string, new_string)

# orig_string = input("Enter the Original String : ")
# old_string = input("Enter the Old String : ")
# new_string = input("Enter the New String : ")          
# print(replace_string(orig_string, old_string, new_string))

# REVERSE A STRING

# def reverse_string(my_string):
#     return my_string[::-1]

# my_string = input("Enter a string : ")
# print(reverse_string(my_string))

# FORMAT A STRING

# def calc_string(first_number, second_number):
#     return f"The sum of {first_number} and {second_number} is {first_number + second_number}."

# first_number = int(input("Enter the First Number : "))
# second_number = int(input("Enter the Second Number : "))
# print(calc_string(first_number, second_number))

# MODIFY A STRING

# def add_product_code(product_code, product_id):
#     if product_code not in product_id:
#         return product_id[:3] + "-" + product_code + "-" + product_id[3:]
#     else:
#         return product_id
        
# product_code = input("Enter Product Code : ")
# product_id = input("Enter Product ID : ")        
# print(add_product_code(product_code, product_id))
            
# Does a string contain all the alphabets

# 1
# from string import ascii_lowercase

# def check_string(my_string):
#     missing = []
#     for alpha in ascii_lowercase:
#         if alpha not in my_string.lower():
#             missing.append(alpha)
            
#     if missing:
#         return f"The string is missing the following letters : {missing}"
#     else:
#         return f"The string contains all the letters."

# my_string = input("Enter the String : ")    
# print(check_string(my_string))

# 2
# def check_string(my_string):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     missing = []
#     for alpha in alphabet:
#         if alpha not in my_string.lower():
#             missing.append(alpha)
            
#     if missing:
#         return f"The string is missing the following letters : {missing}"
#     else:
#         return f"The string contains all the letters."

# my_string = input("Enter the String : ")    
# print(check_string(my_string))

# ANAGRAM

# def is_anagram(first_string, second_string):
#     letters1 = []
#     letters2 = []
#     for letter in first_string.lower():
#         if letter.isalpha():
#             letters1.append(letter)  
#     # print(sorted(letters1))
                  
#     for letter in second_string.lower():
#         if letter.isalpha():
#             letters2.append(letter)
#     # print(sorted(letters2))
        
#     if sorted(letters1) == sorted(letters2):
#         return True
#     else:
#         return False

# first_string = input("Enter the First String : ") 
# second_string = input("Enter the Second String : ")
# print(is_anagram(first_string, second_string))
# # is_anagram("Eleven plus two?", "One plus Twelve?")
# # is_anagram("A cinnamon roll?", "No canola oil, Mr.")
# # is_anagram("root", "TORO")
    
