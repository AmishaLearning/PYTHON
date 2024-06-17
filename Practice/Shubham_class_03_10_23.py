# #rd October 2023

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

# list1 = [1, 2, 3, 4, 5, 45, 3, 23, 24, 5, 6, 6, 4, 33]
# target = 26
# set_box = set()


# for item in range(0, len(list1)):

#     value = target - list1[item]
#     print("Now Value is ", value)     
#     if value in set_box:
#         print("We got the pair", value)
#     else:
#         set_box.add(list1[item])
#         print("Set box contains ",set_box)
#         print("Added value is : ", list1[item])
        
        
# 11th October 2023

# dict1 = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}
# print(dict1.items())

# for key, value in dict1.items():
#     print(key, value)
#     dict1[key] = value + 1
# print(dict1)

# print({key : value + 1 for key, value in dict1.items()})

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = []

# for item in list1:
#     list2.append(item ** 3 + 1)
# print(list2)

# print([item ** 3 + 1 for item in list1])

# Exchange values of key and value

# dict1 = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}
# dict2 = {}
# dict1["E"] = 5
# # dict2 = dict()

# for key, value in dict1.items():
#     print(key, value)
#     dict2[value] = key
# print(dict2)

# Dictionary Comprehension -- creates new dictionary

# dict1 = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}
# dict1["E"] = 5
# print({value : key for key, value in dict1.items()})

dict1 = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}
# dict2 = {}
# dict1["E"] = 5
# dict2 = dict()
# print(dict1["A"])

for key in list(dict1.keys()):
    # print(key, value)
    dict1[dict1[key]] = key
    print(dict1[key])
    del dict1[key]
    print(dict1)

