# itertools.permutations()

# from itertools import permutations

# # print(permutations(['1', '2', '3']))
# # print(list(permutations(['1', '2', '3'])))
# # print(list(permutations(['1', '2', '3'], 2)))
# # print(list(permutations(['abc', 3])))

# s, k = list(map(str, input("Enter the value of s and k : ").split()))
# s = sorted(s)

# for r in range(int(k), int(k) + 1):
#     combinations_r = list(permutations(s, r))
#     for combo in combinations_r:
#         print("".join(combo))

# Compress the string
# string = input("Enter the String : ")
# result = []

# curr_char = string[0]
# char_count = 1

# for i in range(1, len(string)):
#     if string[i] == curr_char:
#         char_count +=1

#     else:
#         result.append(f"({char_count}, {curr_char})")
#         curr_char = string[i]
#         char_count = 1

# result.append(f"({char_count}, {curr_char})")
# print(" ".join(result))

# Validating UID

# num_uid = int(input("Enter the number of UID's : "))

# for x in range(num_uid):
#     uid = input("Enter the UID : ")
#     count_upper = 0
#     count_digit = 0
    
#     for i in uid:
#         if len(uid) == 10 and uid.isalnum() and len(set(uid)) == len(uid):
#             if i.isupper() :
#                 count_upper += 1
#             elif i.isdigit():
#                 count_digit += 1

#     if count_upper >= 2 and count_digit >= 3:
#         print("Valid")
#     else:
#         print("Invalid")
     
# Validating Credit Card Number

# card_num = "4253625879615786"

# if len(card_num) == 16 and card_num.isdigit() and card_num.startswith(('4', '5', '6')):
#     print("Valid")

# number = int(input("Enter the number of Cards numbers : "))
# for num in range(number): 
#     card_num = input("Enter the card Number : ")
#     consecutive_count = 1
#     positions = [4, 9, 14]
#     is_valid = True

#     if len(card_num) == 16 and card_num.isdigit() and card_num[0] in ['4', '5', '6']:
#         for i in range(1, len(card_num)):
#             if card_num[i] == card_num[i - 1] == card_num[i - 2] == card_num[i - 3]:
#                 consecutive_count += 1
#                 if consecutive_count >= 4:
#                     is_valid = False
#                     break
#             else:
#                 consecutive_count = 1

#         for j in positions:
#             if card_num[j] in ['-'] and card_num[j] not in ['_',' ']:
#                 is_valid = False
#                 break
#     else:
#         is_valid = False
        
#     if is_valid:
#         print("Valid")
#     else:
#         print("Invalid")


# number = int(input("Enter the number of Cards numbers : "))
number = 1
for num in range(number):
    # card_num = input("Enter the card Number : ")
    card_num = "4123456789123456"
    consecutive_count = 1
    positions = [4, 9, 14]
    is_valid = True

    if card_num[0] in ['4', '5', '6'] and len(card_num) == 16 and card_num.isdigit():
        for i in range(1, len(card_num)):
            if card_num[i] == card_num[i - 1] == card_num[i - 2] == card_num[i - 3]:
                consecutive_count += 1
                if consecutive_count >= 4:
                    is_valid = False
                    break

        for j in positions:
            if card_num[j] != '-' or card_num[j] in ['-', ' '] :
                is_valid = False
                break
    else:
        is_valid = False

    if is_valid:
        print("Valid")
    else:
        print("Invalid")


# It may have digits in groups of 4, separated by one hyphen "-".----condition not satisfied
    
    

