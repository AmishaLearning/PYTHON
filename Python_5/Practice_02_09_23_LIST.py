# List Programs Part 2

# # Python | Count occurrences of an element in a list

# list1 = [1, 2, 1, 3, 4, 1, 5, 6, 1, 7, 8, 9, 1, 1, 2, 2, 4, 5, 6, 7, 8]
# num = int(input("Enter the number you want to count : "))
# count = 0

# for i in list1:
#     if i == num:
#         count += 1
        
# print(f"The number {num} occurs {count} times in the list")

# Python Program to find sum and average of List in Python

# list2 = [1, 2, 1, 3, 4, 1, 5, 6, 1, 7, 8, 9, 1, 1, 2, 2, 4, 5, 6, 7, 8]

# count = 0

# for i in list2:
#     count += i
    
# print(f"The SUM of the the elements is : {count}")
# # print((f"The SUM is : {sum(list2)}"))

# print("The AVERAGE of the elements is : ", count/len(list2))

# Python | Sum of number digits in List

# list3 = [26, 78, 47, 93]

# print(f"The list is   : {list3}")

# result = []
# for element in list3:
#     sum = 0
#     for digit in str(element):
#         # print("The element is : ",element )
#         sum += int(digit)
#         # print("The digit is :",digit)
#     result.append(sum)
    
# print(f"The result is : {str(result)}")

# # Python | Multiply all numbers in the list

# list4 = [1, 2, 3, 4]
# result = 1

# for i in list4: 
#     result = result * i
# print(f"The Multiplication of all the elements in ths list is : {result}")

# Python program to find smallest number in a list, Python program to find largest number in a list

# list5 = [24, 453, 67, 89, 122, 2, 45, 1, 3217]

# list5.sort()

# print(f"The Sorted list is      : {list5}")
# print(f"The Smallest element is : {list5[0]}")
# print(f"The Largest element is  : {list5[-1]}")

# Python program to find second largest number in a list
# list5 = [24, 453, 67, 89, 122, 2, 45, 1, 3217]
# list5.sort()
# print(f"The list after sorting is    : {list5}")
# list5.remove(list5[-1])
# print(f"The Second Largest Number is : {list5[-1]}")

# Python program to print even numbers in a list

# list5 = [24, 453, 67, 89, 122, 2, 45, 1, 3217, 322, 98, 58]
# list5.sort()
# print(f"The Original list is               : {list5}")
# even = []
# for i in list5:
#     if i % 2 == 0:
#         even.append(i)
# even.sort()
# print(f"The Even numbers from the list are : {even}")

# Python program to print odd numbers in a List

# list5 = [24, 453, 67, 89, 122, 2, 45, 1, 3217, 322, 98, 58]
# list5.sort()
# print(f"The Original list is               : {list5}")
# odd = []
# for i in list5:
#     if i % 2 != 0:
#         odd.append(i)
# odd.sort()
# print(f"The Odd numbers from the list are  : {odd}")

# Python program to print all even numbers in a range, Python program to print all odd numbers in a range
# even = []
# odd = []

# for num in range(1,30):
#     if num % 2 == 0:
#         even.append(num)
#     elif num % 2 != 0:
#         odd.append(num)
        
# print(f"List of Even numbers : {even}")
# print(f"List of Odd numbers  : {odd}")
# even = []

# for num in range(2, 20 , 2):
#     even.append(num)
    
# print(f"The Even numbers are : {even}")

# odd = []

# for num in range(1, 20 , 2):
#     odd.append(num)
    
# print(f"The Odd numbers are  : {odd}")

# # Python program to count Even and Odd numbers in a List
# list6 = [13, 28, 49, 11, 344, 54, 78, 943, 70, 59, 34, 71, 1]

# count_even = 0
# count_odd = 0

# for i in list6:
#     if i % 2 == 0:
#         count_even += 1
#     else: 
#         count_odd += 1
        
# print(f"The count of Even numbers in the list is : {count_even}")
# print(f"The count of Odd numbers in the list is  : {count_odd}")

# # Python program to print all positive numbers in a range, Python program to print all negative numbers in a range

# positive_num = []
# negative_num = []

# start = int(input("Enter the start of range : "))
# end = int(input("Enter the end of range : "))

# for i in range(start, end):
#     if i < 0:
#         negative_num.append(i)
#     else:
#         positive_num.append(i)
        
# print(f"The Positive numbers are : {positive_num}")
# print(f"The Negative numbers are : {negative_num}")


# Python program to count positive and negative numbers in a list

# count_pos = 0
# count_neg = 0

# list7 = [-23, 27, -44, -67, 90, -56, -3, -5, 36, 23, -11]
# print(f"The list is : {list7}")
# for num in list7:
#     if num > 0:
#         count_pos += 1
#     else:
#         count_neg += 1
        
# print(f"The count of Positive numbers is : {count_pos}")
# print(f"The count of Negative numbers is : {count_neg}")

# Remove multiple elements from a list in Python

# list8 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
# list8.sort()

# print(f"Before removing Even numbers : {list8}")

# for i in list8:
#     if i % 2 == 0:
#         list8.remove(i)
        
# print(f"After removing Even numbers  : {list8}")

# # Python | Remove empty tuples from a list
# tuple1 = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('', ''), ()]

# for i in tuple1:
#     if i == ():
#         tuple1.remove(i)
        
# print(tuple1)

# Python | Program to print duplicates from a list of integers

# list9 = [21, 1, 34, 23, 21, 1, 21, 21, 56, 54, 76, 1, 4, 1, 34, 56, 57]
# list9.sort()
# duplicates =[]
# unique = []

# for i in list9:
#     if i not in unique:
#         unique.append(i)
#     elif i not in duplicates:
#         duplicates.append(i)        
         
# print(f"The list of duplicates is : {duplicates}")

# Python – Remove empty List from List
list10 = [5, 6, [], 3, [], [], 9]

# required_list = [x for x in list10 if x]
# print(required_list)

for i in list10[:]:
    if not i :
        list10.remove(i)
print(list10)

