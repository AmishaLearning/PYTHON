# friends = {"Rachel" : "Ross", "Monica" : "Chandler", "Phoebe" : "Joe"}
# print(friends)

# #SOLUTION 1 WITH .items

# for key, value in friends.items():
#     print(key,":",value)
    
# #SOLUTION 2 WITH keys

# for key in friends:
#     print(key, "--", friends[key])
    
# #SOLUTION 3 WITH keys and values

# for i in friends.keys():
#     print(i)
    
# for j in friends.values():
#     print(j)

#SORT DICTIONARY BY VALUES

marks = {"John" : 23, "Lisa" : 56, "Sid" : 48}
#       [   0   : 1  ,  0    :  1,   0   :  1  ]
#Sort based on values and keys
sortedval = sorted(marks.items(), key = lambda x : x[1])# 1 shows sorting based on values and 0 shows sorting done on basis of keys 
print(sortedval)
sortedval = sorted(marks.items(), key = lambda x : x[0])
print(sortedval)

#Sort only with values

v = sorted(marks.values())
print(v)