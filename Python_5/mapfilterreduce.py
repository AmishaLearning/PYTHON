# MAP
# def cube(x):
#     return x * x * x
# print(cube(2))

# list1 = [1, 2, 3, 4, 5, 6]
# new = []

# for i in list1:
#     new.append(cube(i))
# print(new)

# #Shortcut

# def cube(x):
#     return x * x * x

# list1 = [1, 2, 3, 4, 5, 6]
# new = list(map(lambda x : x ** 3, list1))

# print(new)

# FILTER

# list2 = [2, 5, 6, 4, 8, 9]
# def filter_func(a):
#     return a > 4

# list3 = list(filter(filter_func, list2))
# print(list3)

# list3 = list(filter(lambda x : x > 4, list2))
# print(list3)

# REDUCE

# from functools import reduce

# def addition(x, y):
#     return x + y
# numbers = [1, 2, 3, 4, 5]
# # numbers = [3, 3, 4, 5]
# # numbers = [6, 4, 5]
# # numbers = [10, 5]
# # numbers = [15]
# # sum = reduce(lambda x, y : x + y, numbers)
# sum = reduce(addition, numbers)
# print(sum)