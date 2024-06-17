# Find captain's Room

# members_per_grp = int(input("Enter the number of members per group : "))
# room_nums = list(map(int, input("Enter the room numbers : ").split()))

# rooms_count = {}

# for i in room_nums:
#     if i in rooms_count:
#         rooms_count[i] += 1
#     else:
#         rooms_count[i] = 1

# for room, count in rooms_count.items():
#     if count == 1:
#         captains_room = room
#         break
    
# print(captains_room)        


# Check subset

# test_cases = int(input("Enter the number of Test cases : "))


# for i in range(test_cases):
#     num_A = int(input("Enter the numnber of elemensts in Set A : "))
#     set_A = set(map(int, input("Enter the elements of Set A : ").split()))
#     num_B = int(input("Enter the numnber of elemensts in Set B : "))
#     set_B = set(map(int, input("Enter the elements of Set B : ").split()))

#     if set_A.issubset(set_B):
#         print("True")
#     else: 
#         print("False")

# check strict superset

# set_A = set(map(int, input("Enter the elements of set A : ").split()))

# other_sets = int(input("How many other sets u want : "))

# for i in range(other_sets):
#     set_new = set(map(int, input(f"Enter the elements of {i + 1} set : ").split()))
    
# if set_A.issuperset(set_new):
#     print("True")
# else:
#     print("False")

# Polar co-ordinates

# import cmath

# num = input("enter the complex number : ")
# z = complex(num)
# absolute = abs(z)
# print(absolute)
# phase = cmath.phase(z)
# print(phase)

# Word Order

# num_words = int(input("Enter the number of words : "))
# new_words = []

# count = {}

# for i in range(num_words):
#     word = input(f"Enter the {i + 1} word : ")
#     new_words.append(word)

# for i in new_words:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# print(len(set(new_words)))
# print(" ".join(map(str, count.values())))

# Collections deque()
# from collections import deque

# num = int(input("Enter the number of operations : "))
# deque1 = deque()
# for i in range(num):
#     command = list(map(str, input("Enter the operation to be performed : ").split()))
    
#     if command[0] == 'append':
#         value = command[1]
#         deque1.append(value)
#         print(deque1)
        
#     if command[0] == 'appendleft':
#         value = command[1]
#         deque1.appendleft(value)
#         print(deque1)
        
#     if command[0] == 'pop':
#         deque1.pop()
#         print(deque1)
        
#     if command[0] == 'popleft':
#         deque1.popleft()
#         print(deque1)
        
# print(" ".join(map(str, deque1)))
        
# Collections.OrderedDict()

# from collections import OrderedDict

# ordinary_dictionary = {}
# ordinary_dictionary['a'] = 1
# ordinary_dictionary['b'] = 2
# ordinary_dictionary['c'] = 3
# ordinary_dictionary['d'] = 4
# ordinary_dictionary['e'] = 5

# print(ordinary_dictionary)

# ordered_dictionary = OrderedDict()
# ordered_dictionary['a'] = 1
# ordered_dictionary['b'] = 2
# ordered_dictionary['c'] = 3
# ordered_dictionary['d'] = 4
# ordered_dictionary['e'] = 5

# print(ordered_dictionary)
from collections import OrderedDict

num_items = int(input("Enter the number of items : "))
list1 = OrderedDict()

for i in range(num_items):
    
    name_price = list(map(str,input(f"Enter {i + 1} item name and price : ").split()))
    
    name = " ".join(name_price[:-1])
    price = int(name_price[-1])
    
    if name in list1:
        list1[name] += price
    else:
        list1[name] = price
    
for name, price in list1.items():
    print(name, price)
    

