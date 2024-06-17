# print("a" * 4)
# print(4 * "a")

# dict1 = {'A' : 1, "B" : 2}
# dict2 = {'C' : 3, "D" : 4}

# print(dict1.items())

# dict1.update(dict2)
# print(dict1)
# print(dict2)

# dict1.clear()
# print(dict1)

# dict3 = dict2.copy()
# print(dict3)
# print(dict2)

# dict3.pop("C")
# print(dict3)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_comprehension = [x + 10 for x in list1 if x % 2 == 0 or x % 3 == 0 ]
print(list_comprehension)

