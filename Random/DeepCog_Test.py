array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6]



# # array1.append(8)

# array1.extend(array2)
# print(array1)

# def convert(lst):
#    dict1 = {}
#    for i in range(0, len(lst), 2):
#        dict1[lst[i]] = lst[i + 1]
#    return dict1
 
result_dict = dict(zip(array1, array2))
print(result_dict)

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# print(convert(lst))


# dict2 = {"name1" : "ABC",
#          "name2" : "DEF",
#          "name3" : "GHI",
#          "name4" : "JKL"
#          }

# new_value_for_all_keys = [1, 2, 3, 4]

# for key in dict2:
#     dict2[key] = new_value_for_all_keys
# print(dict2)
                             
# print(dict2)