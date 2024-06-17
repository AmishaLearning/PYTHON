# # Using | operator

# dict1 = {"John": 89 , "Lisa": 99}
# dict2 = {"Lisa": 94 , "Peter": 78}

# print(dict1 | dict2)

#Using ** Operator

# dict1 = {"John": 89 , "Lisa": 99}
# dict2 = {"Lisa": 94 , "Peter": 78}

# print({**dict1,**dict2})

#Using copy() and update()

# dict1 = {"John": 89 , "Lisa": 99}
# dict2 = {"Lisa": 94 , "Peter": 78}

# dict3 = dict2.copy()
# dict3.update(dict1)

# print(dict3)
 
#To check if key is already present in Dictionary

friends = {"Rachel" : "Ross", "Monica" : "Chandler", "Phoebe" : "Joe"}

name = "Monica"
if name in friends.keys():
    print("It is present")
    