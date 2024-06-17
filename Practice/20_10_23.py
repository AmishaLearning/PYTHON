# list1 = [1, 1, 2, 3, 2, 3]
# list2 = []

# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     else:
#         pass
# print(list2)

# num = 5
# print(str(num))
# print(type(str(num)))

# import keyword
# print(keyword.kwlist)

# def fun(): 
#     S = 0
#     for i in range(10): 
#         S += i 
#     return S   
# print(fun()) 

# def fun(): 
#     S = 0
  
#     for i in range(10): 
#         S += i 
#         yield S 

# for i in fun(): 
#     print(i) 

# def some_func():
#     print("Inside some_func")
#     # var = 20
#     def some_inner_func():
#         var = 10
#         print("Inside inner function, value of var:",var)
#     some_inner_func()
#     print("Try printing var from outer function: ",var)
# some_func()

# x, y = input("Enter two strings : ").split()
# print("Name1 : ", x)
# print("Name2 : ", y)

# List Comprehension

# x, y = [x for x in input("Enter names : ").split()]
# print("Name1 : ", x)
# print("Name2 : ", y)

# Input separated by ","

# x, y = [x for x in input("Enter names : ").split(",")]
# print("Name1 : ", x)
# print("Name2 : ", y)

# import time
# count_seconds = 4
# for i in range(1, count_seconds + 1):
#     if i > 0 and i < 4:
#         print(i, end='>>>')
#         time.sleep(0.1)
#     else:
#         print('Start')
        
# import time
# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
# 	if i > 0:
# 		print(i, end='>>>')
# 		time.sleep(1)
# 	else:
# 		print('Start')

# a = 12
# b = 12
# c = 2022
# print(a, b, c, sep = "-")

# l = [1, 2, 3, 4, 5, 6]
# # using * symbol prints the list
# # elements in a single line
# print(*l)

# import antigravity

# a, b = 20, 10
# print("Both are equal" if a == b else "a is less than b" if a < b else "a is greater than b")

# gfg = "geeksforgeeks"
# print("".join(reversed(gfg)))

# String = 'GEEKSFORGEEKS'

# print(String[1:5])
# print(String[1:5:2])

# String = 'GEEKSFORGEEKS'

# print(String[-1:-12:-2])

# string = "Amisha Srivastava"
# list_string = list(string)
# reverse_string = []

# for i in list_string[::-1]:
#     reverse_string.append(i)
    
# print("".join(reverse_string))
    
# print(string[::-1])

# list1 = [1, 4, 5, 6, 7]
# for i in range(len(list1)):
#     print(i, list1[i])

# list2 = []
# num = int(input("Enter the number of items in list : "))
# for i in range(num):
#     numbers = int(input("Enter the number : "))
#     list2.append(numbers)
# print(list2)

# random = 1, 2, 3, 4, 5, 6
# print(type(random))

# numbers = [1, 1, 2, 2, 2, 3, 4, 5, 3, 4, 5]
# numbers_1 = [21, 32, 43, 54]
# numbers_set = set(numbers)
# numbers_set.add(12)
# numbers_set.update(numbers_1)
# numbers_set.remove(1)
# union_set = numbers_set.union(numbers_1)
# print(numbers_set)
# print(union_set)

# numbers_frozen = frozenset(numbers)
# union_frozen = numbers_frozen.union(numbers_1)

# print(union_frozen)
# print(numbers_frozen)

# set_1 = {1, 2, 3, 4, 3, 2, 4, 1}
# # for i in range(len(set_1)):
# #     set_1.pop()
# # print(set_1)

# print(True if 12 in set_1 else False)

# dict = {}

# dict[0] = "Geeks"
# dict[1] = "For"
# dict[3] = 1

# print(dict)

# dict["Value_set"] = 2, 3, 4
# print(dict)

# # Key to be added
# key_ref = 'More Nested Things'
# my_dict = {
#     'Nested Things': [{'name', 'thing one'}, {'name', 'thing two'}]
# }
# # Value to be added
# my_list_of_things = [{'name', 'thing three'}, {'name', 'thing four'}]
# # try-except to take care of errors
# # while adding key-value pair
# my_dict[key_ref] = my_list_of_things
# print(my_dict)

