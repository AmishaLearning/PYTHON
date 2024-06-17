# If/ Else Statements
# """ Ordering A Pizza That Verne Can Eat """

# # things that Verne does not eat
# diet_restrictions = set(['meat', 'cheese'])

# # decide which pizza to order
# if 'meat' in diet_restrictions:
#     print('Get a cheese pizza.')

# elif 'meat' and 'cheese' in diet_restrictions:
#     print('Get a vegan pizza.')

# else:
#     print('Get something else.')

# """ Ordering A Pizza That Verne Can Eat """

# # things that Verne does not eat
# diet_restrictions = set(['meat', 'cheese'])

# # decide which pizza to order
# if 'meat' and 'cheese' in diet_restrictions:
#     print('Get a Vegan pizza.')

# elif 'meat' in diet_restrictions:
#     print('Get a Cheese pizza.')

# else:
#     print('Get something else.')

# MATCH STATEMENTS

""" I'll Have the Special! """

# def order_special(day):
#     match day:
#         case 'Sunday':
#             return 'spinach pizza'
#         case 'Monday':
#             return 'mushroom pizza'
#         case 'Tuesday':
#             return 'pepperoni pizza'
#         case 'Wednesday':
#             return 'veggie pizza'
#         case 'Thursday':
#             return 'bbq chicken pizza'
#         case 'Friday':
#             return 'sausage pizza'
#         case 'Saturday':
#             return 'Hawaiian pizza'

# today = 'Friday'
# special = order_special(today)
# print(f'\nToday is {today}, and the special is {special}.\n')

# def order_special(day):
#     match day:
#         case 'Sunday':
#             return 'spinach pizza'
#         case 'Monday':
#             return 'mushroom pizza'
#         case 'Tuesday':
#             return 'pepperoni pizza'
#         case 'Wednesday':
#             return 'veggie pizza'
#         case 'Thursday':
#             return 'bbq chicken pizza'
#         case _:
#             print(f'There is no {day} special')
#             return None
        
# today = 'Christmas'
# special = order_special(today)
# print(f'\nToday is {today}, and the special is {special}.\n')

# FOR LOOPS : we know how many times the loop is running

# """ Loading the Dishwasher """

# # dirty dishes in the sink
# sink = ['bowl', 'plate', 'cup']
# print(f'\nThere are {len(sink)} dishes in the sink: {sink}\n')

# for dish in sink:
#     print(f' - Put a {dish} in the dishwasher')
#     sink.remove(dish)
# # check that the sink is empty
# print(f'\nThere are {len(sink)} dishes in the sink: {sink}\n')

""" Loading the Dishwasher """

# # dirty dishes in the sink
# sink = ['bowl', 'plate', 'cup']
# print(f'\nThere are {len(sink)} dishes in the sink: {sink}\n')

# for dish in list(sink):# added list(sink) here because in previous case once the for loop starts running it takes the first value as 'bowl' then again when the loop runs it take the second value which is now 'cup' as 'bowl is already removed from the list

#     print(f' - Put a {dish} in the dishwasher')
#     sink.remove(dish)
# # check that the sink is empty
# print(f'\nThere are {len(sink)} dishes in the sink: {sink}\n')

# WHILE LOOP : we don't know how many times the loop will run

""" Scrubbing A Stuborn Pan """

# import random

# dirty = True  # state of the pan
# scrub_count = 0  # number of scrubs

# while dirty:
#     scrub_count += 1
#     print(f'Scrubbed the pan {scrub_count} times.')

#     print('Rinsing to check if the pan is clean...\n')

#     if not random.randint(0, 9):
#         print('All clean!')
#         dirty = False
#     else:
#         print('Still dirty...')

# BREAK STATEMENT

""" Putting Away Clean Dishes """

import random

# 20 clean dishes in dishwasher
# dishwasher = ['plate', 'bowl', 'cup', 'knife', 'fork',
#               'spoon', 'plate', 'spoon', 'bowl', 'cup',
#               'knife', 'cup', 'cup', 'fork', 'bowl',
#               'fork', 'plate', 'cup', 'spoon', 'knife']

# for dish in list(dishwasher):
#     # check space left in cabinet
#     if not random.randint(0, 19):
#         print('Out of space!')
#         break
#     else:
#         print(f'Putting {dish} in the cabinet')
#         dishwasher.remove(dish)


# dishwasher = ['plate', 'bowl', 'cup', 'knife', 'fork',
#               'spoon', 'plate', 'spoon', 'bowl', 'cup',
#               'knife', 'cup', 'cup', 'fork', 'bowl',
#               'fork', 'plate', 'cup', 'spoon', 'knife']

# washed_dish = []
# count = 0

# for dish in list(dishwasher):
#     dishwasher.remove(dish)
#     washed_dish.append(dish)
#     count += 1
    
# print(washed_dish)
# print(dishwasher)
# print(count)