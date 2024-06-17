#print all even numbers in a range

# for i in range(2, 25, 2):
#     print(i, end=" ")
    
# #print all odd numbers in a range
# for i in range(1, 25):
#     if i % 2 != 0:
#         print(i, end=" ")
    
    
# #COunt even and odd
# even = 0
# odd = 0

# rangeReq = int(input("Enter the range of numbers : "))
# for i in range(1,rangeReq):
#     if i % 2 == 0:
#         even = even +1
        
#     elif i % 2 != 0:
#         odd = odd + 1
        
# print("Even = {} ".format(even))
# print("Odd = {} ".format(odd))
        
        
# #Removing multiple elements from list

# list1 = [12, 23, 34, 45, 56, 67, 78, 89]

# for i in list1:
#     if i % 2 == 0:
#         list1.remove(i)
        
# print("The new list is : {} ".format(list1))

#Program to print duplicates from a list of integers

# list2 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

# uniquelist = []
# duplicatelist = []

# for i in list2:
#     if i not in uniquelist:
#         uniquelist.append(i)
#     elif i not in duplicatelist:
#         duplicatelist.append(i)
        
# print(duplicatelist)
        
#Count Strings with substring String List

list3 = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms'] 
list4 = str(list3)

sub = 'Geek'
count = 0
for i in list4:
    if sub in i:
        count = count + 1
        
print(count)
        

