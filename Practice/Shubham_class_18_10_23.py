# # To create a blank dictionary

# dict1 = {}
# dict2 = dict()

# # To insert a new key value pair in dictionary 

# A = 100
# dict1["key"] = A
# print(dict1)

# # To insert more than one key value pair

# dict1.update({"B" : 2, "C" : 3, "D" : 4, "E" : 5})
# abc = {"B" : 6, "C" : 7}
# print(dict1)
# abc = {"F" : 6, "G" : 7}
# dict1.update(abc)
# print(dict1)

# # To insert all key value pairs of another dictionary to existing dictionary

# first_dict = {"A" : 1, "X" : 24, "Y" : 25}
# second_dict = {"B" : 2, "C" : 3, "D" : 5, "E" : 21}

# first_dict.update(second_dict)
# print(first_dict)

# # To fetch value of any key from a dictionary

# print(first_dict.get("B"))
# print(first_dict["A"])

# # What if we update a same key again???
# # ans - to maintain uniqueness of the key, it will just update the new value

# first_dict["A"] = 200
# print(first_dict)

# # To delete a key from dictionary

# # del first_dict
# # print(first_dict)

# To fetch the keys of dictionary 

dict1 = {"A" : 1, "B" : 2, "C" : 3}

print(dict1.keys())
print(list(dict1.keys()))
print(list(dict1))

# To fetch values of all the keys from a dictionary

print(dict1.values())
print(list(dict1.values()))

# To fetch both keys and values from a dictionary

print(list(dict1.items()))

# How to take keys from a list and values from anither list and create a dictionary from it

list1 = ["Key1", "Key2", "Key3", "Key4", "Key5"]
list2 = ["Value1", "Value2", "Value3", "Value4", "Value5"]

list2 = [ x + "Amisha" for x in list2]
print(list2)

dict_out = {"Key1" : "value1", "key2" : "value2"}
dict2 = {}

dict1["A"] = 1
print(len(list1))
print(list1[2])

for x in range(len(list1)):
    dict2[list1[x]] = list2[x]
print(dict2)

# Shortcut for the same problem

dict3 = dict(zip(list1, list2))
print(dict3)

## how to check if a specific key is present in a dictionary. Eg, ""key2""

flag = False

for key in dict3:
    if key == "Key2":
        flag = True
        break
print(flag)

# By using "in" operator 

if "Key2" in dict3.keys():
    print(True)
else:
    print(False)