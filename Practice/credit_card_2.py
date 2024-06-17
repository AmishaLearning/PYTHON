   
# num = "5133-3367-8912-3456"
# is_valid = True

# consecutive_count = 0
# num = num.replace("-","")
# print(num)

# for i in range(len(num)):
#     a = num[i]
#     b = num[i - 1]
#     c = num[i - 2]
#     d = num[i - 3]
    
#     if a == b == c == d:
#         consecutive_count += 4
#     else:
#         consecutive_count += 1
# if consecutive_count >= 4:
#     print("Invalid")
# else:
#     print("Valid")

# num = "5133-3367-8912-3456"
# is_valid = True

# consecutive_count = 3
# num = num.replace("-","")
# print(num)

# for i in range(3, len(num)):
#     if num[i] == num[i - 1] == num[i - 2] == num[i - 3]:
#         consecutive_count += 4
#         print("Running from if ")
#         break
#     else:
#         consecutive_count += 1
#         print("running from else ")
#         break
# if consecutive_count >= 4:
#     print("Invalid")
# else:
#     print("Valid")
    
    
num = "5133-3367-8912-3456"
is_valid = True

consecutive_count = 0

for i in range(3, len(num)):
    num = num.replace("-", "")
    if num[i] == num[i - 1] == num[i - 2] == num[i - 3]:
        consecutive_count += 1
        break

if consecutive_count >= 1:
    print("Invalid")
else:
    print("Valid")

