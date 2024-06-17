#APPROACH 1 USING sort()
# list1=[21,34,12,45,54,86]
# list1.sort()

# print("The First  largest number in the list is : ",list1[-1])
# print("The Second largest number in the list is : ",list1[-2])

#APPROACH 2 
list2=[99,12,34,56,33]
list3=set(list2)
list3.remove(max(list3))

print("The list with the First Maximum Value removed : ",list3)
print("The Second Maximum Value is : ",max(list3))
