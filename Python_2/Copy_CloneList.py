#APPROACH 1 USING SLICING TECHNIQUE
# list1=[4,8,2,10,15,18]
# print("The Original List is :",list1)
# list1_copy=list1[:]
# print("The Copied List is   :",list1_copy)

#APPROACH 2 USING extend() method

# list2=[4,8,2,64,67,9]
# print("The Original List is :",list2)
# list3=[12,45,90]
# list3.extend(list2)
# print("The Copied List is   :",list3)

#APPROACH 3 USING list() method
# list3=[34,65,37,87]
# print("The Original List is :",list3)
# list4=list(list3)
# print("The Copied List is   :",list4)

#APPROACH 4 USING copy() method

# list5=[26,74,92,50]
# print("The Original List is :",list5)
# list6=list5.copy()
# print("The Copied List is   :",list6)

#APPROACH 5 USING  list comprehension
list7=[75,48,95,34]
print("The Original List is :",list7)
list8=[i for i in list7 ]
print("The Copied List is   :",list8)