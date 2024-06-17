# # importing "keyword" for keyword operations
# import keyword
 
# # printing all keywords at once using "kwlist()"
# print("The list of keywords is : ")
# print(keyword.kwlist)

# a = 4
# b = 0
# print("The value of a / b is : ")
# assert b != 0, "Divide by 0 error"
# print(a / b)


# program illustrates the use of docstrings
 
# def helloWorld():
#   # This is a docstring comment
#     """ This program prints out hello world """ 
#     print("Hello World")
 
 
# helloWorld()
# print(helloWorld.__doc__)

# # Python3 code to demonstrate variable assignment
# # upon condition using Conditional Operator

# # Initialising variables using Conditional Operator
# a = 1 if 20 > 10 else 0

# # Printing value of a
# print("The value of a is: " , str(a))


# Python program showing how to
# multiple input using split
 
# # taking two inputs at a time
# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
 
# # taking three inputs at a time
# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)
 
# # taking two inputs at a time
# a, b = input("Enter two values: ").split()
# print("First number is {} and second number is {}".format(a, b))
 
# # taking multiple inputs at a time
# # and type casting using list() function
# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of students: ", x)

# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)

# print([i**j for i in range(1,5) for j in range(1,4)])

# x, y = [int(x) for x in input("Enter two values: ").split(",")]
# print("First Number is: ", x)
# print("Second Number is: ", y)

# import time
 
# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end='>>>')
#         time.sleep(1)
#     else:
#         print('Start')

# import time
 
# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end='>>>', flush = True)
#         time.sleep(1)
#     else:
#         print('Start')


#code for disabling the softspace feature
# print('G','F','G', sep='')
 
# #for formatting a date
# print('09','12','2016', sep='-')
 
# #another example
# print('pratik','geeksforgeeks', sep='@')

# a, b = 10, 20

# print("a is equal to b " if a == b else "a is greater than b " if a > b else "a is less than b ")

#Any Returns true if any of the items is True. It returns False if empty or all are false.

# # Since all are false, false is returned
# print (any([False, False, False, False]))
 
# # Here the method will short-circuit at the
# # second item (True) and will return True.
# print (any([False, True, False, False]))
 
# # Here the method will short-circuit at the
# # first (True) and will return True.
# print (any([True, False, False, False]))

# # All Returns true if all of the items are True (or if the iterable is empty).
# # All can be thought of as a sequence of AND operations on the provided iterables.

# # Here all the iterables are True so all
# # will return True and the same will be printed
# print (all([True, True, True, True]))

# # Here the method will short-circuit at the
# # first item (False) and will return False.
# print (all([False, True, True, False]))

# # This statement will return False, as no
# # True is found in the iterables
# print (all([False, False, False]))

# list1 = []
# list2 = []
 
# # case 1
# if (list1 == list2):
#     print("True")
# else:
#     print("False")
 
# # case 2
# if (list1 is list2):
#     print("True")
# else:
#     print("False")
    
# #Output is false because two empty lists are at different memory locations

# string = "madam"

# reverse1 = [string[i] for i in range(len(string)-1, -1, -1)]

# print("Original string is : ",string)
# reverse2 = "".join(reverse1)
# print("Reversed string is : ",reverse2)

# if string == reverse2:
#     print("Palindrome ")
    
# else:
#     print("Not a Palindrome")
    
# if string[0::] == string[::-1]:
#         print("Palindrome ")
# else:
#     print("Not a Palindrome")
    
    
# List = [['Geeks', 'For'], ['Geeks']]

# print("Accessing a element from a Multi-Dimensional list")
# print(List[0][1])
# print(List[1][0])
    
    
# odd_sqr = [i ** 2 for i in range(1,11) if i % 2 == 1]
# print(odd_sqr)

# Define the list to be used for the demonstration
# test_list = [1, 4, 5, 7, 8]

# length = sum(1 for _ in test_list)

# print("Length of list using list comprehension is:", length)

# tuple1 = tuple("Geeksforgeeks")
# print(tuple1[0:])

set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}

print(set1.difference(set2))
print(set2.difference(set1))