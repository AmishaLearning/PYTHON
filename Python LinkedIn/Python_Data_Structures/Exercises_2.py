# EXERCISE 4

# recent_orders = []
# item = int(input("Enter the number of items you want to add : "))
# for order in range(1, item + 1):
#     recent_orders.append(input(f"Enter item {order} you want to add : "))
#     print(recent_orders)
#     if len(recent_orders) > 5 :
#         print("Order exceeded length of 5...Removing intial orders")
#         recent_orders.pop(0)
#         print(recent_orders)

# EXERCISE 5

# def palindrome_check():
#     string = input("Enter a string to check for palindrome : ").lower()
#     if string[::] == string[::-1]:
#         return f"Yes!! the string '{string.upper()}' is a PALINDROME"
#     else:
#         return f"No!! the string '{string.upper()}' is NOT A PALINDROME"
    
# print(palindrome_check())

# EXERcISE 6
# 04_01b.py

# def menu():

#     nadias_list = {
#         "BEV003" :	"Cafe Latte",
#         "STA001" : "Panko Stuffed Mushrooms",
#         "STA002" :	"Mini Cheeseburgers",
#         "STA003" :	"French Onion Soup",
#         "STA004" :	"Artichokes with Garlic Aioli",
#         "STA005" :	"Parmesan Deviled Eggs",
#         "SAL001" :	"Garden Buffet",
#         "SAL002" :	"House Salad",
#         "SAL003" :	"Chefs Salad",
#         "SAL004" :	"Quinoa Salmon Salad",
#         "ENT001" :	"Classic Burger",
#         "ENT002" :	"Tomato Bruschetta Tortellini",
#         "ENT003" :	"Handcrafted Pizza",
#         "ENT004" :	"Barbecued Tofu Skewers",
#         "ENT005" :	"Fiesta Family Platter",
#         "DES001" :	"Creme Brulee",
#         "ENT001" :	"Classic Burger",
#         "DES002" :	"Cheesecake",
#         "DES003" :	"Chocolate Chip Brownie",
#         "DES004" :	"Apple Pie",
#         "STA001" :	"Panko Stuffed Mushrooms",
#         "DES005" :	"Mixed Berry Tart",
#         "DES005" :	"Mixed Berry Tart",
#         "BEV001" :	"Tropical Blue Smoothie",
#         "BEV002" :	"Pomegranate Iced Tea",
#         "DES005" :	"Mixed Berry Tart",
#         "BEV003" :	"Cafe Latte",
#         "DES005" :	"Mixed Berry Tart",
#         "BEV003" :	"Cafe Latte"
#     }  
    
#     list_keys = ["BEV003", "STA001", "STA002", "STA003", "STA004",
#         "STA005" , "SAL001", "SAL002", "SAL003", "SAL004",
#         "ENT001" ,"ENT002" ,"ENT003" ,"ENT004" , "ENT005" , "DES001" ,
#         "ENT001" ,"DES002" ,"DES003" ,"DES004" ,"STA001" ,"DES005" ,"DES005" , "BEV001" ,"BEV002" ,"DES005" ,"BEV003" ,"DES005" ,  "BEV003"]
#     count_total_items(list_keys)   
#     print(f"Before removing duplicates the value is : {len(list_keys)}")
#     beverages(list_keys)
    

# def count_total_items(list_keys):
#     dict1 = {}
#     for item in list_keys:
#         if item in dict1:
#             dict1[item] = dict1[item] + 1
#         else:
#             dict1[item] = 1
    
# def beverages(list_keys):
#     beverages_list = []
#     starters_list = []
#     desert_list = []
#     salad_list = []
#     entree_list = []
#     for item in list_keys:
#         if item.startswith("BEV") :
#             beverages_list.append(item)
#         elif item.startswith("STA"):
#             starters_list.append(item)
#         elif item.startswith("DES"):
#             desert_list.append(item)
#         elif item.startswith("SAL"):
#             salad_list.append(item)
#         elif item.startswith("ENT"):
#             entree_list.append(item)
                
#     print(f"The beverages are : {set(beverages_list)}")
#     print(f"The staters are : {set(starters_list)}")
#     print(f"The deserts are : {set(desert_list)}")
#     print(f"The salads are : {set(salad_list)}")
#     print(f"The entree are : {set(entree_list)}")
#     total_items = len(set(beverages_list)) + len(set(starters_list)) + len(set(salad_list)) + len(set(desert_list)) + len(set(entree_list))
#     print(f"After removing duplicates the value is : {total_items}")
# menu()

