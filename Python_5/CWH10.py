#Dictionary

# dic = {
#     "Amisha" : "Human Being",
#     "Spoon"  : "Object"
# }

# print(dic["Amisha"])

# emp = {
#     123 : "Harry",
#     234 : "Hermione",
#     345 : "Ron"
# }

# print(emp[123])

# info = {"Name": "Amisha", "Gender" : "Female", "Age" : 25}
# print(info)
# print(info["Name"])
# print(info.get("Age"))#if value not available, None will be printed instead of any error

#Accessing all keys or values together
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print("The value corresponding to {} is {}".format(key,info[key]))
#     print(f"The value corresponding to {key} is {info[key]}.....")
    
# print(info.items())
# for key, value in info.items():
#     print(f"The value corresponding to {key} is {value}.....")

#UPDATE()
#Dictionary is ordered
ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}

# ep1.update(ep2)

#CLEAR() -- gives empty dictionary
# ep1.clear()
# print(ep1)

#POP() -- one removes key value pairs 

# ep1.pop(122)
# print(ep1)

#POPITEM() -- removes last key value pair from dictionary

# ep1.popitem()
# print(ep1)

#del -- deletes the complete dictionary
# del ep1
# print(ep1)

del ep1[122]
print(ep1)
