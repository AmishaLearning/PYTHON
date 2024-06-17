#APPROACH 1
# list1=[12,23,34,45]
# print("List Before Clearing :",list1)
# list1 *=0 #Deletes all the elements
# print("List After Clearing :",list1)

#APPROACH 2
# list2=[24,35,46,57,68]
# print("List Before Clearing :",list2)
# list2=[]
# print("List After Clearing :",list2)

#APPROACH 3
# list3=[98,76,54,21]
# print("List Before Clearing :",list3)
# list3.clear()
# print("List After Clearing :",list3)

#APPROACH 4
list4=[87,76,54,74]
print("List Before Clearing :",list4)
del list4[1:3]
print("List After Clearing range of elements :",list4)
del list4[:]
print("List Before Clearing :",list4)
