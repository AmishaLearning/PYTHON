# Detect floating point number

# num = int(input("Enter the number of test cases : "))

# for i in range(num):
#     string = input("Enter the string : ")
    
#     starts_with_valid_char = string.startswith(('+', '-', '.')) or (string[0].isdigit() and '.' in string)
#     decimal_point_count = string.count('.')
    
#     try:
#         float_value = float(string)
#         no_exception = True
#     except ValueError:
#         no_exception = False
        
#     is_valid = starts_with_valid_char and decimal_point_count == 1 and no_exception

#     if is_valid:
#         print(True)
#     else:
#         print(False)

# Re.split()

# regex_pattern = "[,.]"	# Do not delete 'r'.

# import re
# print("\n".join(re.split(regex_pattern, input("Enter the Pattern : "))))

# import calendar

# month, day, year = map(int, input("Enter the date as month, day, year : ").split())
# day_name = calendar.day_name[calendar.weekday(year, month, day)]
# print(day_name.upper())

# itertools.combinationns()

# from itertools import combinations

# # print(list(combinations('12345',2)))
# # A = [1, 1, 3, 3, 3]
# # print(list(combinations(A, 4)))


# def print_combinations(S, k):
#     S = sorted(S)  # Sort the input string to ensure lexicographic order
#     for r in range(1, k + 1):
#         combinations_r = list(combinations(S, r))
#         for combo in combinations_r:
#             print(''.join(combo))

# S, K = list(map(str,input("Enter the string: ").split()))
# print_combinations(S, int(K))

# s, k = list(map(str, input("Enter the value of s and k : ").split()))
# s = sorted(s)

# for r in range(1, int(k) + 1):
#     combinations_r = list(combinations(s, r))
#     for combo in combinations_r:
#         print("".join(combo))

# itertools.combinations_with_replacement(iterable, r)

from itertools import combinations_with_replacement

s, k = list(map(str, input("Enter the value of s and k : ").split()))
s = sorted(s)

for r in range(int(k), int(k) + 1):
    combinations_r = list(combinations_with_replacement(s, r))
    for combo in combinations_r:
        print("".join(combo))
