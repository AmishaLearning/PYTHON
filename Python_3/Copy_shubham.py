
import copy

# list1 = [1,2,3,4,5,["Amisha","Srivastava"]]
# # a = 10
# # b = a
# # a = a + 1
# list2 = list1
# # list1.append("Amisha")
# print(list1)
# print(list2)


# list3 = list1.copy() ### [1, 2, 3, 4, 5]

# print(id(list1[1]))
# print(id(list3[1]))

# list1[-1].append("Misha")
# print(list1)
# print(list3)

list1 = [1,2,3,4,["Amisha", "Srivastava"]]
list4 = copy.deepcopy(list1)

print(list1)
print(list4)

list1[-1].append("shubham")

print(list1)
print(list4)

print(list1[-1])
print(id(list1[-1]))

print(list4[-1])
print(id(list4[-1]))
