# OrderedDict()

# from collections import OrderedDict

# print("This is a Dict : \n")
# dict1 = {}
# dict1['a'] = 1
# dict1['b'] = 2
# dict1['c'] = 3
# dict1['d'] = 4

# for key, value in dict1.items():
#     print(key, value)
# print()
# print("This is a Ordered Dict : \n")
# dict2 = OrderedDict()
# dict2['A'] = 1
# dict2['B'] = 2
# dict2['C'] = 3
# dict2['D'] = 4

# for key, value in dict2.items():
#     print(key, value)

# Python – Insertion at the beginning in OrderedDict

# from collections import OrderedDict

# # Approach 1
# ordered_dict1 = OrderedDict([('Apple', '10'),('Mango', '15')])
# ordered_dict2 = OrderedDict([('Banana', '20'),('Orange', '25')])
# ordered_dict2.update(ordered_dict1)
# print(ordered_dict2)

# # Approach 2
# # ordered_dict1.update({'Pomegranate': '30'})
# # ordered_dict1.move_to_end('Pomegranate', last = False)
# # print(ordered_dict1)

# Find common elements in three sorted arrays by dictionary intersection

from collections import OrderedDict

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

lst = []

dict1 = OrderedDict.fromkeys(ar1)
dict2 = OrderedDict.fromkeys(ar2)
dict3 = OrderedDict.fromkeys(ar3)

for values1, keys1 in dict1.items():
    for values2, keys2 in dict2.items():
        for values3, keys3 in dict3.items():
            if values1 == values2 == values3:
                lst.append(values1)
print("List with common elements: ",lst)
