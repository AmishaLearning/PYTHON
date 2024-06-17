# list1 = [12, 23, 34, 45, 56, 67, 78 ,89]
# print("List before clearing : ", list1)

# while len(list1) != 0:
#     list1.pop()

# print("List after clearing  : ", list1)

#In other words, this slicing operation creates a new empty list. 
#It effectively "clears" the original list lst because it creates a new list containing no elements.

list2 = [12, 23, 34, 45, 56, 67, 78]
list2 = list2[:0]
print(list2)    

