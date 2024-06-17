# #[1,1,1,2,4,8,3,9,27,4,16,64]
# print([i**j for i in range(1,5) for j in range(1,4)])

# str1 = "Testing python programming Language" 
#Output {'o': x, 'i': x, 'a': x, 'e': x, 'u': x}
# str="Testing python programming Language"
# str1= str.replace(" ","")

# vowels=['a','e','i','o','u']

# dict1={}
# for x in str1:
#     if x in vowels:
#         if x in dict1:
#             dict1[x] = dict1[x] + 1
#         else:
#             dict1[x] = 1
# print(dict1)
    
def count(list1):
    a = 0
    b = 0
    
    for i in list1:
        if i % 2 == 0:
            a = a + 1
        else:
            b = b + 1
    return a,b

list1=[20, 25, 14, 16, 19, 24, 28, 47, 26]
a,b = count(list1)
print("Even is {} and Odd is {}".format(a,b))            
    
# from numpy import *

# m=matrix('1 2 3 ; 2 3 4 ; 5 6 7')
# print(m)

# for i in range(4):
#     for j in range(i+1):
#         print("# ", end="")
#     print()

# word=str(input("Enter a string :"))

# if word[0::]==word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# from collections import Counter   
# str1 = "Testing python programming Language"
# x=str(input("Ebter the alphabet you want to find occurrance of :"))
# dic=Counter(str1)
# print("'{}' has occurred {} times. ".format(x,dic[x]) )