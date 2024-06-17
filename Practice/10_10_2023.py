# ZOO

# word = input("Enter the String : ")
# count_x = 0
# count_y = 0

# for i in word:
#     if i == "z" or i == "Z":
#         count_x += 1
#     if i == "o" or i == "O":
#         count_y += 1
# print(f"Count of Z : {count_x}, Count of O : {count_y}")

# if (2 * count_x == count_y):
#     print("Yes")
# else:
#     print("No")

# DIVISIBILITY

# size_list = int(input("Enter the size of the list : "))
# numbers = list(map(int, input("Enter the numbers : ").split()))

# numbers_list = list(numbers)
# print("List of Numbers is : ", numbers_list)

# integers = []

# for i in numbers_list:
#     num = i % 10
#     integers.append(num)

# print("Integers are : ", integers)
# number = "".join(map(str, integers))
# print(f"Number is : {number} ")

# if (int(number)) % 10 == 0:
#     print("Yes")
# else:
#     print("No")

# COST OF BALLOON 

# test_cases = 2  

# for i in range(test_cases):  
#     # Total Price of Green considering cost for Green
#     total_price_green_green = 0 
    
#     # Total Price of Purple considering cost for Purple
#     total_price_purple_purple = 0
    
#     # Total Price of Green considering cost for Purple
#     total_price_green_purple = 0
    
#     # Total Price of Purple considering cost for Green
#     total_price_purple_green = 0
    
    
#     balloon_cost = list(map(int, input("Enter cost of Green and Purple Balloon : ").split()))
#     balloon_cost_green, balloon_cost_purple = balloon_cost[0], balloon_cost[1]
#     participants = int(input("Enter the number of participants : "))
      
#     for j in range(participants):
#         choice = list(map(int, input("Enter 1 for solving 0 for not solving : ").split()))
#         choice_green, choice_purple = choice[0], choice[1]
        
#         if choice_green == 1:
#             price_green_green = choice_green * balloon_cost_green
#             total_price_green_green += price_green_green
        
#         if choice_purple == 1:
#             price_purple_purple = choice_purple * balloon_cost_purple
#             total_price_purple_purple += price_purple_purple
        
#         if choice_green == 1:
#             price_green_purple = choice_green * balloon_cost_purple
#             total_price_green_purple += price_green_purple
                        
#         if choice_purple == 1:
#             price_purple_green = choice_purple * balloon_cost_green
#             total_price_purple_green += price_purple_green

#     print("Total Price Green (Cost Green) : ", total_price_green_green)
#     print("Total Price Purple (Cost purple) : ", total_price_purple_purple)
    
#     print()
    
#     print("Total Price Green (Cost Purple) : ", total_price_green_purple)  
#     print("Total Price Purple (Cost Green) : ", total_price_purple_green)

#     Final_Green_Ballon_Price = total_price_green_green + total_price_purple_purple
#     Final_Purple_Ballon_Price = total_price_green_purple + total_price_purple_green

#     print(min(Final_Green_Ballon_Price, Final_Purple_Ballon_Price))

# SEVEN SEGMENT DISPLAY -- Incomplete

# test_cases = int(input("Enter number of Test Cases : "))

# for i in range(test_cases):
#     input_num = int(input("Enter the number : "))

#     if input_num == 0 or input_num == 6 or input_num == 9:
#         sticks = 6
#     elif input_num == 1:
#         sticks = 2
#     elif input_num == 2 or input_num == 3 or input_num == 5:
#         sticks = 5
#     elif input_num == 4:
#         sticks = 4
#     elif input_num == 7:
#         sticks = 3
#     elif input_num == 8:
#         sticks = 7
        
#     if sticks == 2:
#         print("Maximum number is : ", 1)
#     elif sticks == 3:
#         print("Maximum number is : ", 7)
#     elif sticks == 4:
#         print("Maximum Number is : ", 11)
#     elif sticks == 5:
#         print("Maximum Number is : ", 5)
#     elif sticks == 6:
#         print("Maximum number is : ", 111)
#     elif sticks == 7:
#         print("Maximum Number is : ", 3)
#     elif sticks == 8:
#         print("Maximum Number is : ", 1111)
#     elif sticks == 9:
#         print("Maximum Number is : ", 9)

# ALI AND HELPING INNOCENT PEOPLE

# String = input("Enter String : ")
# vowels = ["A", "E", "I", "O", "U", "Y"]
# is_valid = True

# def Valid(input_string):
#     if len(input_string) == 9 and input_string[2] not in vowels:
#         string_list = list(input_string)
#         for i in range(len(string_list) - 1):
#             try:
#                 num1 = int(string_list[i])
#                 num2 = int(string_list[i + 1])
                
#                 sum = num1 + num2
               
#                 if sum % 2 != 0:
#                     return False
#             except Exception as e:
#                 pass
#         return True
#     else:
#         return False  

# if Valid(String):
#     print("valid")
# else:
#     print("invalid")


            






     
        
    