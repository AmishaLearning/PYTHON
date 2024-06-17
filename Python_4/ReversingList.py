#REVERSING USING SLICING

# list1 = [12, 23, 34, 45, 56, 67, 78, 89]
# print("List before Reversing : ",list1)

# list1[0::] = list1[::-1]
# print("List after Reversing  : ",list1)

#USING reverse()

list2 = [13, 24, 35, 46, 68, 79]
print("List before Reversing : ",list2)

print("List after Reversing  : ", list(reversed(list2)))