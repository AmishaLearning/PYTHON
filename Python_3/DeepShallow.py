from copy import copy,deepcopy
list1=[1,2,[3,5],4]

#Shallow Copy

list2=copy(list1)
list2[3]=7
list2[2].append(6)
print(list2)
print(list1)

#Deep Copy 

list3=deepcopy(list1)
list3[3]=8
list3[2].append(7)
print(list3)
print(list1)

