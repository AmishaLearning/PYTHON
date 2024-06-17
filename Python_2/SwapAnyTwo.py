#APPROACH 1
# list1=[33,2,5,44,7,3,89]

# print("Before Swapping : ",list1)

# x=int(input("Position 1 to be swapped :"))
# y=int(input("Position 1 to be swapped :"))

# list1[x],list1[y]=list1[y],list1[x]

# print("After  Swapping : ",list1)

#APPROACH 2

list2 = [12,32,43,65]
print("Before Swapping : ",list2)

pos1 = int(input("Enter Position 1 : "))
pos2 = int(input("Enter Position 2 : "))

x = list2.pop(pos1)
y = list2.pop(pos2-1)
 
list2.insert(pos1,y)
list2.insert(pos2,x)

print("After  Swapping : ",list2)