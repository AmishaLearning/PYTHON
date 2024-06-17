#APPROACH 1
# list1=[12,23,34,45]
# print("Sum of the elements is :",sum(list1))

#APPROACH 2 USING loop with range()
list2=[5,10,15,20]
total=0

for i in range(0,len(list2)):
    total=total+list2[i]
    
print("The sum of the elements is : ",total)    