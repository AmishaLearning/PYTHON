#APPROACH 1
# list1=[12,34,67,90,57]
# n=int(input("Enter Number to Find : "))
# flag=0

# for i in range(0,len(list1)):
#     if list1[i] == n:
#         print("Element Found")
#         flag=1
#         break
# if (flag==0):
#     print("Element Not Found ")

#Flag used in order to get only found result otherwise it will print both found and not found as result

#APPROACH 2

list2 = [23,45,67,89]
n = int(input("Enter the number you want to find : "))

print("Found" if n in list2 else "Not Found")