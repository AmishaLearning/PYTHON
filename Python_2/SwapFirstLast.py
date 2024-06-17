#APPROACH 1
# list1=[22,3,1,4,6,7,4]
# list1[0],list1[-1]=list1[-1],list1[0]
# print(list1)

#APPROACH 2
# list2=[12,22,11,21,36,9,7]
# print("Before Swapping : ",list2)
# temp=list2[0]
# # print(temp)
# list2[0]=list2[-1]
# # print(list2[0])
# list2[-1]=temp
# # print(list2[-1])
# print("After  Swapping : ",list2)

#APPROACH 3
list3=[5,3,88,6,4,7,6]
start,*middle,end=list3

list3=[end,*middle,start]
print(list3)