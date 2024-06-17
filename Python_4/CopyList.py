# # Using the Slice Operator
# list1 = [12, 23, 34 , 45, 56, 67 ,78, 89]
# list1_copy = list1[:]
# print("The list 1 is         {}. ".format(list1))
# print("The Copy of list 1 is {}. ".format(list1_copy))


# # Using the in-built function extend()
# list2 = [13, 24, 35, 46, 57, 68 ,79]
# list2_copy = []
# list2_copy.extend(list2)

# print(list2_copy)

# Using list comprehension

list3 = [14, 25, 36, 47 ,58, 69, 90]

list3_copy = [i for i in list3]
print(list3_copy)