# Python program to check whether the string is Symmetrical or Palindrome

# str1 = input("Enter the String : ")

# if str1[0::] == str1[::-1]:
#     print("Yes!! Its a Palindrome") 
# else:
#     print("No! Its not a Palindrome")

# Reverse words in a given String in Python

# str2 = input("Enter a String : ")
# # str2 = "My name is Amisha Srivastava"
# list1 = str2.split()

# list2 = list1[::-1]
# result = " ".join(list2)
# print(result)

# Ways to remove i’th character from string in Python

# test_str = "GeeksForGeeks"
# new_str = test_str[:2] + test_str[3:]
# print("The string after removal of i'th character : " + new_str)

# Find length of a string in python 

# str2 = input("Enter a String : ")
# print(f"Length of the String is : {len(str2)}")

# str2 = input("Enter a String : ")
# count = 0

# for i in str2:
#     count += 1
# print(f"The length of the string is : {count}")    

# Python – Avoid Spaces in string length

# str2 = input("Enter a String : ")
# print(f"The original string is : '{str2}' and the length is : '{len(str2)}'")

# str3 = str2.replace(" ", "")
# print(f"The string after removing spaces is : '{str3}' and the length is : '{len(str3)}'")

# Python program to print even length words in a string

# str3 = "Today is 6th of September which is a Wednesday!"
# list1 = str3.split(' ')
# new_str = []

# for i in list1:
#     if len(i) % 2 == 0:
#         new_str.append(i)

# print(f"The even length words in the string are : '{new_str}'")

# Python – Uppercase Half String

# str4 = "Today is 6th of September which is a Wednesday!"
# print(f"The original String is           : {str4}")

# half_index = len(str4) // 2
# result = str4[:half_index] + str4[half_index:].upper()

# print(f"The String after modification is : {result}")

# Python program to capitalize the first and last character of each word in a string
# str5 = "my name is amisha srivastava"
# list2 = str5.split()
# result = []
# print(f"String before modification : {str5}")

# for i in list2:
#     x = i[0].upper()+i[1:-1]+i[-1].upper()
#     result.append(x)
    
# result = " ".join(result)
# print(f"String after modification  : {result}")

# Python program to check if a string has at least one letter and one number

# def checkstring(str):
#     letter = False
#     number = False
    
#     for i in str:
#         if i.isalpha():
#             letter = True
#         if i.isdigit():
#             number = True
#     return letter and number

# print(checkstring("ami12sha"))
# print(checkstring("amisha"))

# Python | Count the Number of matching characters in a pair of string

# str6 = "amisha"
# str7 = "aarushi"
# list1 = []

# for i in str6:
#     if i in str7:
#         list1.append(i)
      
# print(f"The list of matching characters is  : {list(set(list1))}")
# print(f"The count of matching characters is : {len(set(list1))}")

# Python program to count number of vowels using sets in given string

# str8 = "amisha"
# vowels = "aeiou"
# count = 0
# for i in str8:
#     if i in vowels:
#         count += 1

# print(f"The number of vowels in the string is : {count}")

# Python Program to remove all duplicates from a given string

# str9 = "geeksforgeeks"
# result = set(str9)

# print(str(result))

# str9 = "amisha srivastava"
# result = ""
# print(f"The string before removing duplicates is : {str9}")
# for i in str9:
#     if i not in result:
#         #If 'i' is not in 'result', add it to 'result'
#         result += i
# print(f"The string after removing duplicates is  : {result}")

# Python – Least Frequent Character in String, Python | Maximum frequency character in String
# Python – Odd Frequency Characters
    
str10 = "geeksforgeeks"
new_str = {}

for i in str10:
    if i in new_str:
        new_str[i] += 1
    else:
        new_str[i] = 1

min_count = min(new_str.values())
max_count = max(new_str.values())
min_chars = []
max_chars = []
odd_chars = []

for i, count in new_str.items():
    if count == min_count:
        min_chars.append(i)
    if count == max_count:
        max_chars.append(i)
    if count % 2 != 0:
        odd_chars.append(i)     

print(f"The values are: {new_str}")
print(f"The characters with minimum count are : {min_chars}")
print(f"The characters with maximum count are : {max_chars}")
print(f"The characters with odd     count are : {odd_chars}")
