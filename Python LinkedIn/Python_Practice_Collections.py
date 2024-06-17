# DEDUPLICATE THE LISTS

# def deduplicate(my_list):
#     return sorted(set(my_list))

# my_list = input("Enter the items : ").split()
# print(deduplicate(my_list))

# MODIFY A TUPLE

# def modify_tuple(my_tuple, new_value, index):
#     return my_tuple[:index] + (new_value,) + my_tuple[index:]

# sports = ('football', 'basketball', 'cricket', 'hockey', 'tennis', 'volleyball')
# new_value1 = 'baseball'
# index1 = 2

# numbers = (7, 17, 13, 19, 5)
# new_value2 = 11
# index2 = 3
# print(modify_tuple(sports, new_value1, index1))   
# print(modify_tuple(numbers, new_value2, index2))    

# def build_menu(key, value):
#     cakes = {
#         100 : ["Carrot", 1.99],
#         101 : ["Chocolate", 1.99],
#         102 : ["Strawberry", 2.19],
#         103 : ["Spice", 2.29],
#         104 : ["Vanilla", 1.79]
#     }
#     cakes[key] = value
#     result = []
#     for cake_value in cakes.values():
#         result.append(f"{cake_value[0]} Cake - ${cake_value[1]}")
#         result_list = sorted(result)

#     result_final = result_list[::-1]
#     return result_final

# key = int(input("Enter Key value : "))
# value1 = input("Enter the Cake name : ")
# value2 = float(input("Enter the price : "))
# print(build_menu(key, [value1, value2]))

# def build_menu(key, value):
#     cakes = {
#         100 : ["Carrot", 1.99],
#         101 : ["Chocolate", 1.99],
#         102 : ["Strawberry", 2.19],
#         103 : ["Spice", 2.29],
#         104 : ["Vanilla", 1.79]
#     }
#     cakes[key] = value
#     result = []
#     for cake_value in cakes.values():
#         result.append(f"{cake_value[0]} Cake - ${cake_value[1]}")
#     return list(reversed(sorted(result)))
        
# key = int(input("Enter Key value : "))
# value1 = input("Enter the Cake name : ")
# value2 = float(input("Enter the price : "))
# print(build_menu(key, [value1, value2]))

# def find_winner(player_scores):
#     player_scores = {
#         'Arthur' : [85, 90, 92],
#         'Bela'   : [75, 80, 85],
#         'Carol'  : [90, 92, 95],
#         'Deepak' : [87, 89, 91]
#     }
#     average_score = []
#     for value in player_scores.values():
#         average = sum(value) / len(value)
#         average_score.append(average)
        
#     average_score_dict = dict(zip(player_scores.keys(), average_score))
#     print(average_score_dict)
#     print(max(average_score_dict.values()))
    
# print(find_winner(12))

def find_winner(player_scores):
    player_scores = {
        'Arthur' : [85, 90, 92],
        'Bela'   : [75, 80, 85],
        'Carol'  : [90, 92, 95],
        'Deepak' : [87, 89, 91]
    }
    highest_avg = 0
    highest_avg_player = ""
    for player, scores in player_scores.items():
        avg = sum(scores)/ len(scores)
        if avg > highest_avg:
            highest_avg = avg
            highest_avg_player = player
    return [highest_avg_player, highest_avg]

result = find_winner(12)
print(result)
    
# string = "amisha"
# string = string.replace("a", "A")
# print(string)

# string = "my name is amisha"
# string_new = string.replace(" ","")
# print(string_new)
# vowles = ['a', 'e', 'i', 'o', 'u']
# result = {}

# for value in string_new:
#     if value in vowles:
#         if value in result:
#             result[value] = result[value] + 1
#         else:
#             result[value] = 1
            
# print(result)

food_items = {
    'fruits': {
        'tropical': {
            'mango': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'vitamin A', 'fiber']
            },
            'pineapple': {
                'color': 'yellow',
                'taste': 'tangy',
                'nutrients': ['vitamin C', 'manganese', 'fiber']
            }
        },
        'temperate': {
            'apple': {
                'color': 'red',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'fiber', 'potassium']
            },
            'pear': {
                'color': 'green',
                'taste': 'juicy',
                'nutrients': ['vitamin C', 'fiber', 'copper']
            }
        }
    },
    'vegetables': {
        'leafy': {
            'spinach': {
                'color': 'green',
                'taste': 'earthy',
                'nutrients': ['vitamin K', 'vitamin A', 'iron']
            },
            'kale': {
                'color': 'green',
                'taste': 'bitter',
                'nutrients': ['vitamin K', 'vitamin A', 'calcium']
            }
        },
        'root': {
            'carrot': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin A', 'vitamin K', 'fiber']
            },
            'beet': {
                'color': 'red',
                'taste': 'earthy',
                'nutrients': ['vitamin C', 'folate', 'iron']
            }
        }
    }
}
# def describe_items(food_items, color):
#     list1 = []
#     for food_type, food_type_data in food_items.items():
#         for climate, items in food_type_data.items():
#             for item, item_data in items.items():
#                 color = item_data['color']
#                 taste = item_data['taste']
#                 if color == color_input:
#                     # print(item, color)
#                     list1.append(f"The {item} is {taste}.")
#     print(list1)
            
                
# color_input = input("Enter Color of ur Choice : ")  
# describe_items(food_items, color_input)

# def describe_food(food_items, color):
#     result = []
#     for food in food_items:
#         for type in food_items[food]:
#             for fru_veg in food_items[food][type]:
#                 # print(fru_veg)
#                 if food_items[food][type][fru_veg]['color'] == color:
#                     result.append(f"The {fru_veg} is {food_items[food][type][fru_veg]['taste']}.")
#     return result
# color = input("Enter color of ur choice : ")
# print(describe_food(food_items, 'red'))
            
            
my_list = [1, 2, 3, 4, 5]
my_list_1 = [2, 4, 6, 8]

my_list_set = set(my_list)

# my_list_frozenset = frozenset(my_list)

# my_list_set.add(7)
# print(my_list_set[3])

# print(my_list_frozenset.union(my_list_1))
# print(my_list_frozenset.intersection(my_list_1))
# print(my_list_frozenset.difference(my_list_1))
# print(my_list_frozenset.symmetric_difference(my_list_1))
# print(my_list_frozenset.issuperset(my_list_1))
# print(my_list_frozenset.isdisjoint(my_list_1))
# print(my_list_frozenset.copy())

# my_list_set.add(7)
# print(my_list_set)

# union automatically converts the list my_list_1 to set 
# print(my_list_set.union(my_list_1))
# print("****", my_list_set)
# my_list_set.update(my_list_1)
# print("###", my_list_set)

# my_list_set.discard(5)
# print(my_list_set)
my_list_set.difference_update(my_list_1)
print(my_list_set)
my_list_set.difference(my_list_1)
print(my_list_set)