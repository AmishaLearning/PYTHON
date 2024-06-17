# EXERCISE 1
# Required Results 

# paragraph = """Nadia’s Garden Restaurant is the creation of husband and wife team Nadia and Timothy Arbore. 
# Their American-infused, Italian-based, organically created, cuisine was inspired by Nadia’s papa, an immigrant from Italy, 
# who shared his love of cooking with Nadia as a young girl. His focus on using fresh ingredients and family style dining were 
# the inspiration for Nadia’s Garden Restaurant. Located in the heart of Main Streets Historic District, they are proud to be a 
# part of a rich community. In 2011, the duo remodeled the restaurant and updated their menu to include newer and more diverse entrées
# that could be made from local organic suppliers. Preservation of the building’s original layout has allowed them to create smaller, 
# more intimate, dining spaces. Nadia and Timothy are committed to sharing their family history of cuisine, along with their new inspirations,
# with their customers. Their passion for community, entertainment, and hospitality are found in every aspect of Nadia’s Garden Restaurant."""
 
# para_1 = paragraph.lower()
# para_1 = para_1.replace(".", "")
# para_1 = para_1.replace("’", "")
# para_1 = para_1.replace(",", "")
# print(para_1)

# list_words = para_1.split()
# print(list_words)
# print(len(list_words))
# print("****")
# print(set(list_words))
# print(len(set(list_words)))

# dict1 = {}

# for word in list_words:
#     if word in dict1:
#         dict1[word] = dict1[word] + 1
#     else:
#         dict1[word] = 1
        
# print(dict1)

# Program :: Count words from a paragraph

# def para():
#     paragraph = """Nadia’s Garden Restaurant is the creation of husband and wife team Nadia and Timothy Arbore. Their American-infused, Italian-based, organically created, cuisine was inspired by Nadia’s papa, an immigrant from Italy, who shared his love of cooking with Nadia as a young girl. His focus on using fresh ingredients and family style dining were the inspiration for Nadia’s Garden Restaurant. Located in the heart of Main Streets Historic District, they are proud to be a part of a rich community. In 2011, the duo remodeled the restaurant and updated their menu to include newer and more diverse entrées that could be made from local organic uppliers. Preservation of the building’s original layout has allowed them to create smaller, more intimate, dining spaces. Nadia and Timothy are committed to sharing their family history of cuisine, along with their new inspirations,with their customers. Their passion for community, entertainment, and hospitality are found in every aspect of Nadia’s Garden Restaurant."""
#     print(count_words(paragraph))     

# def count_words(para_1):
#     para_1 = para_1.lower()
#     para_1 = para_1.replace("’", "").replace(".", "").replace(",", "")
#     list_words = para_1.split()
    
#     dict1 = {}
#     for word in list_words:
#         if word in dict1:
#             dict1[word] = dict1[word] + 1
#         else:
#             dict1[word] = 1 
#     # print(list_words)
#     # print(len(list_words))
#     return dict1
# para()

# EXERCISE 2

# def counting_products():
#     products_purchased = ["DES005",
#             "BEV003",
#             "DES004",
#             "DES001",
#             "DES002",
#             "DES003",
#             "DES002",
#             "DES002",
#             "STA004",
#             "SAL004",
#             "ENT005",
#             "BEV003",
#             "SAL002",
#             "ENT005",
#             "SAL004",
#             "ENT004",
#             "ENT004",
#             "DES004",
#             "BEV001",
#             "STA001",
#             "STA003",
#             "BEV002",
#             "STA003",
#             "DES005",
#             "BEV002",
#             "ENT004",
#             "ENT001",
#             "DES005",
#             "ENT004",
#             "STA005",
#             "ENT005",
#             "DES002",
#             "ENT001",
#             "SAL001",
#             "BEV001",
#             "DES002",
#             "BEV001",
#             "DES004",
#             "ENT004",
#             "DES001",
#             "STA005",
#             "DES004",
#             "ENT002",
#             "DES001",
#             "ENT002",
#             "ENT003",
#             "BEV001",
#             "DES004",
#             "STA005",
#             "STA003",
#             "SAL002",
#             "ENT001",
#             "SAL004",
#             "STA005",
#             "ENT002",
#             "DES004",
#             "DES004",
#             "SAL001",
#             "BEV003",
#             "DES001"]
#     # print(get_common_products(products_purchased)) 
#     print(get_top_three_common_products(products_purchased)) 
    
# def get_common_products(products_purchased):
#     dict1 = {}
#     for items in products_purchased:
#         if items in dict1:
#             dict1[items] = dict1[items] + 1 
#         else:
#             dict1[items] = 1
   
#     max_key = 0
#     max_value = 0 
    
#     for key, value in dict1.items():
#         if value > max_value:
#             max_key = key
#             max_value = value
#     return f"The Key with maximum value {max_value} is {max_key}"        
# counting_products()

# def get_top_three_common_products(products_purchased):
#     dict1 = {}
#     for item in products_purchased:
#         if item in dict1:
#             dict1[item] += 1
#         else:
#             dict1[item] = 1

#     # Sort the dictionary by values in descending order
#     sorted_dict = sorted(dict1.items(), key=get_value, reverse=True)
#     print(sorted_dict)
#     # Get the top three items
#     top_three = sorted_dict[:3]

#     return f"The top three most common products are: {top_three}"

# def get_value(item):
#     return item[1]

# counting_products()

# EXERCISE 3
# sell 5 starters, 3 salads, and 3 entrees
# make 9 more starters and 1 more entree

# def inventory():
#     dict_inventory = {
#         'STA001' : 10,
#         'SAL002' : 20,
#         'ENT004' : 13
#     }
#     print("Seeling details : ")
#     print("-------------------------------------------------")
#     sell_starters(dict_inventory)
#     print("Remaining Starters : ",dict_inventory['STA001'])
#     print("-------------------------------------------------")
#     sell_salads(dict_inventory)
#     print("Remaining Salads : ",dict_inventory['SAL002'])
#     print("-------------------------------------------------")
#     sell_entree(dict_inventory)
#     print("Remaining Entree : ",dict_inventory['ENT004'])
#     print("-------------------------------------------------")
#     print("Adding items to Inventory : ")
#     print("-------------------------------------------------")
#     add_starters(dict_inventory)
#     print("Total Count Starters : ",dict_inventory['STA001'])
#     print("-------------------------------------------------")
#     add_entree(dict_inventory)
#     print("Total Count Entree : ",dict_inventory['ENT004'])    
#     print("-------------------------------------------------")
    
# def sell_starters(starters_purchased):
#     count_starter = 0
#     for key, value in starters_purchased.items():
#         if key == 'STA001':
#             while count_starter < 5:
#                 starters_purchased[key] -= 1
#                 count_starter += 1
#             print(f"Sold {count_starter} starters and {starters_purchased[key]} are leftover")
                
# def sell_salads(salads_purchased):
#     count_salads = 0
#     for key, value in salads_purchased.items():
#         if key == 'SAL002':
#             while count_salads < 3:
#                 salads_purchased[key] -= 1
#                 count_salads += 1
#             print(f"Sold {count_salads} salad and {salads_purchased[key]} are leftover")
            
# def sell_entree(entree_purchased):
#     count_entree = 0
#     for key, value in entree_purchased.items():
#         if key == 'ENT004':
#             while count_entree < 3:
#                 entree_purchased[key] -= 1
#                 count_entree += 1
#             print(f"Sold {count_entree} entree and {entree_purchased[key]} are leftover")
            
# def add_starters(starters_added):
#     count_added_starter = 0
#     for key, value in starters_added.items():
#         if key == "STA001":
#             while count_added_starter < 9:
#                 starters_added[key] += 1
#                 count_added_starter += 1
#             print(f"Added {count_added_starter} starters now the count is {starters_added[key]}")

# def add_entree(entree_added):
#     count_added_entree = 0
#     for key, value in entree_added.items():
#         if key == "ENT004":
#             while count_added_entree < 1:
#                 entree_added[key] += 1
#                 count_added_entree += 1
#             print(f"Added {count_added_entree} starters now the count is {entree_added[key]}")          
      
# inventory()

