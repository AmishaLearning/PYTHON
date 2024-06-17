# 17 < 17
# 15 == 5 * 3

# Challenge 

# user_input = input("What's My Favourite Food? : ")

# if user_input == "Pani Puri":
#     print("Yep! So Amazing!")
# else:
#     print("Yuck! That's not it!")

# print("Thanks for Playing! ")

# Car Wash

# def function(parameter)
# function_call(arguments)
# def wash_car(amount_paid): # amount_paid is a parameter
#     if (amount_paid == 12):
#         print("Wash with white foam")
#         print("Rinse Once")
#         print("Air Dry")
        
#     if (amount_paid == 6):
#         print("Wash with tri-color foam")
#         print("Rinse Twice")
#         print("Dry with large blow dryer")

# wash_car(12)# 12 here is an "argument : values we give to our functions"


# Withdraw Money

# def withdraw_money(current_balance, amount):
#     if (current_balance >= amount):
#         current_balance = current_balance - amount
#     print("The balance is :", current_balance)
    
# withdraw_money(100, 80)

# def withdraw_money(current_balance, amount):
#     if (current_balance >= amount):
#         current_balance = current_balance - amount
#         # print(current_balance)
#         return current_balance
    
# balance = withdraw_money(100, 80)
# # print("**", balance)
# if balance <= 50:
#     print("We need to make a deposite!!")
# else:
#     print("Nothing to See Here!!")

# Favourite City

def favourite_city(name):
    print(f"One of my favourite cities is {name}")

favourite_city("Bangalore")
favourite_city("Raebareli")
favourite_city("Lucknow")