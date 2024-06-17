# Find words which are greater than given length k

# str1 = "Hello! Today is Thursday and its the month of September"
# list1 = str1.split()

# limit = 4
# result = []

# for i in list1:
#     if len(i) >= limit:
#         result.append(i)

# print(f"The elements having length more than {limit} are : {result}")

# Python program for removing i-th character from a string

# str2 = input("Enter the string           : ")
# start = int(input("Enter Start of String : "))
# end = int(input("Enter End of String     : "))

# result = str2[start:end]
# print(f"The result of string starting from {start} and ending at {end} is : {result}")

# Python program to split and join a string

# str3 = "Geeks For Geeks"
# list_string = str3.split(" ")    

# result = "-".join(list_string)
# print(result)

# Python | Check if a given string is binary string or not

# str4 = "1001110101010001"

# # Initialize a flag to check if all characters are either '0' or '1'
# is_binary = True

# for char in str4:
#     if char != '0' and char != '1':
#         is_binary = False
#         break

# if is_binary:
#     print("Yes")
# else:
#     print("No")

# def checking(str4):
#     check = set(str4)
#     set1 = {'1', '0'}   
#     for i in check:
#         if i in set1:
#             return "Yes its a Binary String"
#         else:
#             return "No its not a Binary String"

# str4 = "1001120101010001"        
# print(checking(str4))
    
# Python program to find uncommon words from two Strings

# str5 = "Today is September 7 and its a Thursday"
# str6 = "Yesterday was September 6 and it was a Wednesday"
# print(f"The First  String is : {str5}")
# print(f"The Second String is : {str6}")

# list1 = str5.split()
# list2 = str6.split()
# uncommon = []

# # for i in list1:
# #     if i not in list2:
# #         uncommon.append(i)
        
# # print(f"The elements which are not present in Second String  are : {list(set(uncommon))}")

# for i in list2:
#     if i not in list1:
#         uncommon.append(i)
        
# print(f"The elements which are not present in First String are : {list(set(uncommon))}")

# Python | Swap commas and dots in a String

# str7 = "Hello, I am fine."

# a = ","
# b = "."
# a, b = b, a
# print(f"Hello{a} I am fine{b}")
