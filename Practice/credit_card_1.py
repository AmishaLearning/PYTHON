# Credit Card Validation ---Initial Code

# Hacker rank Code

# def is_valid_credit_card(card_num):
#     is_valid = True
    
# # Must
#     def exact_length(num):
#         result = len(num) == 16
#         return result        
    
#     # Must    
#     def starts_with_valid_prefix(num):
#         result = num[0] in ('4', '5', '6')
#         return result
    
#     # Must
#     def contains_invalid_character(num):
#         for i in num:
#             if i == '_' or i == " ":
#                 result = True
#                 return result
#         result = False
#         return result
        
#     # Must
#     def all_digits(num):
#         if num[4] == '-' and num[9] == '-' and num[14] == '-':
#             num = num.replace("-","")
#         result = num.isdigit()
#         return result
    
#     # Must
#     def has_consecutive_identical_digits(num): 
#         num = num.replace("-", "")         
#         consecutive_count = 0
#         for i in range(1, len(num)):
#             if num[i] == num[i - 1] == num[i - 2] == num[i - 3]:
#                 consecutive_count += 1
#                 if consecutive_count >= 1:
#                     result = True
#                     return result
#         result = False
#         return result
    
#     # May
#     def has_valid_grouping(num):    
#         result = False    
#         if len(num) < 20 and num[4] == '-' and num[9] == '-' and num[14] == '-':
#             result = True
#         return result
    
#     if exact_length(card_num) and starts_with_valid_prefix(card_num)  and all_digits(card_num)  and not contains_invalid_character(card_num) and not has_consecutive_identical_digits(card_num):
#         return is_valid
    
#     elif has_valid_grouping(card_num) and starts_with_valid_prefix(card_num) and all_digits(card_num) and not contains_invalid_character(card_num) and not has_consecutive_identical_digits(card_num):
#         return is_valid

# num = int(input())

# for i in range(num):
#     card_num = input()
#     if is_valid_credit_card(card_num):
#         print("Valid")
#     else:
#         print("Invalid")

########################################################################################################################################

def is_valid_credit_card(card_num):
    is_valid = True
    
# Must
    def exact_length(num):
        result = len(num) == 16
        print("exact_length                     : ", result)
        return result        
    
    # Must    
    def starts_with_valid_prefix(num):
        result = num[0] in ('4', '5', '6')
        print("starts_with_valid_prefix         : ", result)
        return result
    
    # Must
    def contains_invalid_character(num):
        for i in num:
            if i == '_' or i == " ":
                result = True
                print("contains_invalid_character       : ", result)
                return result
        result = False
        print("contains_invalid_character       : ", result)
        return result
        
    # Must
    def all_digits(num):
        if num[4] == '-' and num[9] == '-' and num[14] == '-':
            num = num.replace("-","")
        result = num.isdigit()
        print("all_digits                       : ", result)
        return result
    
    # Must
    def has_consecutive_identical_digits(num):
        num = num.replace("-","")
        consecutive_count = 0
        for i in range(1, len(num)):
            if num[i] == num[i - 1] == num[i - 2] == num[i - 3]:
                consecutive_count += 1
                if consecutive_count >= 1:
                    result = True
                    print("has_consecutive_identical_digits : ", result)
                    return result
        result = False
        print("has_consecutive_identical_digits : ", result)
        return result
    
    # May
    def has_valid_grouping(num):    
        result = False    
        if len(num) < 20 and num[4] == '-' and num[9] == '-' and num[14] == '-':
            result = True
            print("has_valid_grouping               : ", result)
        return result
    
    if exact_length(card_num) and starts_with_valid_prefix(card_num)  and all_digits(card_num)  and not contains_invalid_character(card_num) and not has_consecutive_identical_digits(card_num):
        print("I am from part 1")
        return is_valid
    
    elif has_valid_grouping(card_num) and starts_with_valid_prefix(card_num) and all_digits(card_num) and not contains_invalid_character(card_num) and not has_consecutive_identical_digits(card_num):
        print("I am from part 2")
        return is_valid

num = int(input("Enter the number of Credit card Numbers : "))

for i in range(num):
    card_num = input("Enter the card number : ")

    if is_valid_credit_card(card_num):
        print("Valid")
    else:
        print("Invalid")

