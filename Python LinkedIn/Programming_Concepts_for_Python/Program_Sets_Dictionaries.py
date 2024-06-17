# SETS : Unordered collection of unique Objects

# college = set(['Bill', 'Katy', 'Verne', 'Dillon', 'Bruce', 'Olivia', 'Richard', 'Jim'])

# coworker = set(['Aaron', 'Bill', 'Brandon', 'David', 'Frank', 'Connie', 'Kyle', 'Olivia'])

# family = set(['Garry', 'Landon', 'Larry', 'Mark', 'Olivia', 'Katy', 'Rae', 'Tom'])

# print(college)
# print(len(college))
# print(len(coworker))
# print(len(family))

# friends = college.union(coworker, family)
# print(friends)
# print(len(friends))

# common_friends = college.intersection(coworker, family)
# print(common_friends)

# SORT SETS

# set of all friends
# friends = set(['Mark', 'Rae', 'Verne', 'Richard',
#                'Aaron', 'David', 'Bruce', 'Garry',
#                'Bill', 'Connie', 'Larry', 'Jim',
#                'Landon', 'Dillon', 'Frank', 'Tom',
#                'Kyle', 'Katy', 'Olivia', 'Brandon'])

# # set of people who live in my zip code
# zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
#                'Rudolph', 'Bill', 'Olivia', 'Jim',
#                'Lindsay', 'Rae', 'Mark', 'Kramer',
#                'Landon', 'Newman', 'George'])

# set of people who play Munchkin
# munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
#                  'Mark', 'Landon', 'Rae'])

# # set of Olivia's friends
# olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])

# local = friends.intersection(zipcode)
# print(local)

# invite = local.difference(munchkins)# friends only present in local
# print(invite)

# invite = invite.symmetric_difference(olivia)# the uncommon friends in both of the sets
# print(invite)

# invited_friends = set(['Nestor', 'Amanda', 'Olivia'])
# print('Verne' in invited_friends)

# invited_friends.add('Verne')
# print(invited_friends)
# invited_friends.add('Olivia')
# print(invited_friends)

# invited_friends.remove("Nestor")
# print(invited_friends)
# # invited_friends.remove("Nestor")
# # print(invited_friends)

# print(invited_friends.pop())
# print(invited_friends.pop())
# print(invited_friends.pop())
# print(invited_friends.pop())

# DICTIONARIES

# dictionary of name/number pairs
# rolodex = {'Aaron': 5556069,
#            'Bill': 5559824,
#            'Dad': 5552603,
#            'David': 5558331,
#            'Dillon': 5553538,
#            'Jim': 5555547,
#            'Mom': 5552603,
#            'Olivia': 5556397,
#            'Verne': 5555309}

# print(rolodex['Verne'])
# print(hash('Verne'))

# Adding items to Dictionary
# print(rolodex['Amanda']) throws error as Amanda is not there in the dict
# rolodex['Amanda'] = 5559754
# print(rolodex['Amanda'])

# print(rolodex['David'])
# rolodex['David'] = 5550902
# print(rolodex['David'])
# # Dictionaries don't allow duplicate keys

# rolodex['David'] = (5558331, 5550902)
# print(rolodex['David'])

# rolodex['David'] = 5558331
# print(rolodex['David'])

# rolodex['David(Amanda)'] = 5550902
# print(rolodex['David(Amanda)'])

# Reverse Lookup Issues

# rolodex = {'Aaron': 5556069,
#            'Bill': 5559824,
#            'Dad': 5552603,
#            'David': 5558331,
#            'Dillon': 5553538,
#            'Jim': 5555547,
#            'Mom': 5552603,
#            'Olivia': 5556397,
#            'Verne': 5555309}

# def caller_id(lookup_number):
#     for name, number in rolodex.items():
#         if number == lookup_number:
#             return name
        
# print(caller_id(5556397))
# # print(caller_id(8675309))
# print(caller_id(5552603))


