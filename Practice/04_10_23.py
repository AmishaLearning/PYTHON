# MEDIAN OF TWO SORTED ARRAY

# num1 = [1, 2]
# num2 = [3, 0.5]

# num1.extend(num2)
# num3 = sorted(num1)

# median = 0
# def median_len_odd(list1):
#     middle = list1[len(list1) // 2]
#     median = middle
#     return median

# def median_len_even(list2):
#     middle1 = list2[(len(list2) // 2) - 1]
#     middle2 = list2[len(list2)// 2]
#     median = (middle1 + middle2) / 2
#     return median

# if len(num3) % 2 == 0:
#     result = median_len_even(num3)
#     print(f"Median : {result}")
# else:
#     result = median_len_odd(num3)
#     print(f"Median : {result}")

# TRIPLET SUM -- able to find only starting pair not all

# nums = [-1,0,1,2,-1,-4]

# for i in range(0, len(nums) - 2):
#     if nums[i] + nums[i + 1] + nums[i + 2] == 0:
#         print(nums[i], nums[i + 1], nums[i + 2])
#         break
#     else:
#         print([])

# LETTER COMBINATIONS OF A PHONE NUMBER

# dict1 = {2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
# result = []
# digits = input("Enter digits of ur choice : ")
# digits_list = list(digits)

# item_1 = dict1[int(digits_list[0])]
# item_2 = dict1[int(digits_list[1])]

# item_1_list = list(item_1)
# item_2_list = list(item_2)

# for i in item_1_list:
#     for j in item_2_list:
#         words = i, j
#         result.append(words)
# output_list = []
# for i in result:
#     output_list.append("".join(i))
# print(output_list)

# SUM OF FOUR -- not getting all pairs

# nums = [1,0,-1,0,-2,2]
# target = 0
# result = []
# for i in range(0, len(nums) - 3):
#     if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] == target:
#         all_nums = nums[i], nums[i + 1], nums[i + 2], nums[i + 3]
#         result.append(list(all_nums))
# print(result)


        