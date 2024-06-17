# VALID PARENTHESIS

# def is_valid(string):
#     stack = []
#     mapping = { ")" : "(", "}" : "{", "]" : "[" }
    
#     for char in string:
#         print("char is : ", char)
#         if char in mapping:
#             print("Char 2 is : ", char)
#             if stack:
#                 print(stack)
#                 top_elemennt = stack.pop()
#                 print("Top Element : ",top_elemennt)
#             else:
#                 top_elemennt = "#"
#             if mapping[char] != top_elemennt:
#                 print("Top element : ", top_elemennt)
#                 return False
#         else:
#             stack.append(char)
#             print(stack, "**")
#     return len(stack) == 0

# input_string = "{[()]}"

# if is_valid(input_string):
#     print("Valid")
# else:
#     print("Invalid")

# MERGE TWO SORTED LIST

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# list2.extend(list1)
# print(sorted(list2))

# SWAP NODES IN PAIRS

# list1 = [1, 2, 3, 4]
# list1[0], list1[1] = list1[1], list1[0]
# list1[2], list1[3] = list1[3], list1[2]
# print(list1)

# FIND THE INDEX OF FIRST OCCURRENCE IN A STRING

# string = "butsadbut"
# string_match = "sad"
# if string_match in string:
#     print(string.index(string_match))

# from itertools import permutations

# list1 = [1, 2, 3]
# permutations_list = list(permutations(list1))
# print(permutations_list)

