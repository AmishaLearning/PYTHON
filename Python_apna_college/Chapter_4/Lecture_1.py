 # Dictionary
 
# print ("--------------------------------Dictionary-----------------------------")
# dict1 = {
#     "name" : "amisha",
#     "cgpa" : 9.8,
#     "year" : 2023,
#     "is_adult" : True
# }
# print(dict1)

# dict2 = {
#     "name" : "apnaCollege",
#     "subjects" : ['python', "c", "java"],
#     "topics" : {"dict" , "set"},
# }
# print(dict2)
# print(type(dict2))

# print(dict2["subjects"])

# dict2["name"] = "Amisha"
# dict2["name"] = "Aarushi" # overwrites the previous value
# print(dict2)

# dict2["surname"] = "srivastava"
# print(dict2)

# print("--------------------------------Empty Dict-------------------------------")
# null_dict = {}
# print(null_dict)

# null_dict["name"] = "Aarushi"
# null_dict["surname"] = "srivastava"
# print(null_dict)

# print("---------------------------Nested Dictionary-------------------------------")

# student = {
#     "name" : "amisha",
#     "score" : {
#         "chem" : 78,
#         "phy"  : 89,
#         "math" : 90
#     }
# }
# print(student)
# print(student["score"])
# print(student["score"]["chem"])

# print("--------------------------Methods------------------------------")
# student = {
#     "name" : "amisha",
#     "score" : {
#         "chem" : 78,
#         "phy"  : 89,
#         "math" : 90
#     },
#     "subjects" : ["chem", "phy", "math"]
# }
# print(student.keys())
# print(list(student.keys()))
# print(len(student.keys()))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# print(list(student.items()))

# pairs = list(student.items())
# print(pairs[0])

# print("------------------------------printing keys------------------------------")

# If the key is wrong , then the first statement will show error and execution will fail, but the second stat  ement will return None, thw execution will not stop.
# print(student["name"])
# print(student.get("name"))

# student.update({"city": "delhi"})
# print(student)
# new_dict = {"day": "Thursday"}
# student.update(new_dict)
# print(student)

# print("---------------------------Update value with same key------------------------")
# student.update({"name": "neha kumar"})
# print(student)

# print("------------------------Sets------------------------")

# collection = {1, 2, 3, 4, "hello", "world", 2, 3}
# print(collection)
# print(type(collection))
# print(len(collection))

# print("-----------------------Empty Sets------------------------")

# set1 = {}
# print(type(set1))
# set2 = set()
# print(type(set2))

# print("-----------------------Set Methods------------------------")

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(1) # valuw will not be added as it is duplicate
# collection.add((3, 4, 5))
# collection.add("apnacollege")
# collection.add(7)
# collection.add(9)
# # collection.add([1, 2, 3]) # list cannot be added as it is mutable
# print(collection)

# collection.remove(1)
# print(collection)
# print("Popped value :", collection.pop()) # removes a random value
# print(collection)
# print(len(collection))
# collection.clear()
# print(len(collection))

# print("-------------------------Unoin Intersection------------------------")

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.union(set2)) # returns new set , doesn't make changes in the original sets

# print(set1.intersection(set2)) 
# print(set1)
# print(set2)

