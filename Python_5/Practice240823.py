# # Swap two numbers

# a = int(input("Enter the Value of a : "))
# b = int(input("Enter the Value of b : "))
# print(f"Before Swapping a = {a} and b = {b}")

# a, b = b , a

# print(f"After Swapping a = {a} and b = {b}")

# # Check number is prime or not

# num = int(input("Enter a number : "))
# count = 0

# if num > 1:
#     for i in range(1, num +1):
#         if num % i == 0:
#             count += 1
            
#     if count == 2:
#         print("Number is Prime")
#     else: 
#         print("Not Prime")

# # Factorial 

# fact = 1
# num = int(input("Enter the number : "))

# for i in range(1,num + 1):
#     fact = fact * i
# print(fact)

# # Fibonacci Series

# num = int(input("Enter number till where u want series : "))
# a = 0
# b = 1
# if num < 1:
#     print("Fibonacci Not possible")
    
# elif num == 1:
#     print(a)
    
# else:
#     print(a, end = " ")
#     print(b, end = " ")
#     for i in range(1, num + 1):
#         c = a + b
#         a = b
#         b = c
#         print(c, end = " ")

# # Find sum of element in an array
# arr = []
# n = int(input("Enter the number of elements you want in the array : "))

# for i in range(1, n + 1):
#     num = int(input(f"Enter the {i} number : "))
#     arr.append(num)

# print(f"The sum of the elements in the array is : {sum(arr)}")

# #Length of list

# list1 = [12, 34, 45 ,56 ,67 ,78 ,89]
# count = 0

# for i in list1:
#     count += 1
    
# print(f"The length of the list {list1} is : {count} ")

# # Remove the nth occurrence of the word from a list

# list2 = ["Geeks", "for", "Geeks"]
# word = "Geeks"
# n = 2
# count = 0

# for i in range(0, len(list2)):
#     if list2[i] == word:
#         count += 1
#         if count == n:
#             del list2[i]
# print(list2)

# # Search an element in the list

# list3 = [12, 23, 34, 45, 56, 67, 78, 89]
# element = 45
# flag = False
# for i in list3:
#     if i == element:
#         flag = True
#         break
# if flag:
#     print("Element Found")
# else:
#     print("Not Found")

# # String Palindrome
# string = input("Enter a string : ")
# reverse = string[::-1]

# if string == reverse:
#     print("Yes!! Its a palindrome")
    
# else: 
#     print("No!!Its not a palindrome")

# #Reverse words in string

# string2 = "Welcome to the World of Programming"
# words = string2.split()

# words2 = words[-1::-1]

# reverse_string = " ".join(words2)
# print(reverse_string)

# # Clear the list

# list4 = [12, 23, 34, 45, 56, 67, 78, 89]

# for i in range(len(list4)):
#     list4.pop()
    
# print(list4)

# # Program to add two matrices using nested loop
 
# X = [[1,2,3],
#     [4 ,5,6],
#     [7 ,8,9]]
 
# Y = [[9,8,7],
#     [6,5,4],
#     [3,2,1]]
  
# result = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(X)):
#     for j in range(len(Y)):
#         result[i][j] = X[i][j] + Y[i][j]

# for r in result:
#     print(r)


# Remove specific character using string

# String = "Hello World!"
# String2 = String.replace("Hello", "Amisha")
# print(String2)

# # Word frequency in String
# String3 = "25 August is the 24th day in the month of August , August is about to end"
# word = "August"
# list1 = String3.split()
# print(list1)
# count = 0

# for i in list1:
#     if i == word:
#         count += 1

# print(f"The word {word} occurs {count} times in the string " )

# Remove a key from dictionary 

test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
 
print("The dictionary before performing remove is : ", test_dict)

del test_dict['Mani']

print("The dictionary after remove is             : ", test_dict)
