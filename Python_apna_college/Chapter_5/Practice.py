# print("-------------------------------Practice_5--------------------------------")
# print("\n")

# print("--------------------------------Question_1--------------------------------")

# i = 1
# while i <= 100: # stopping condition
#     print("The number is : ", i)
#     i += 1
# print("Loop Ended")

# print("--------------------------------Question_2--------------------------------")

# i = 100
# while i >= 1:
#     print("The Number is :", i)
#     i -= 1
# print("Loop Ended")

# print("--------------------------------Question_3--------------------------------")

# num = int(input("Enter a number : "))
# i = 1

# while i <= 10:
#     print(f"{num} X {i} = {num * i}")
#     i += 1 

# print("----------------------------------Question_3--------------------------------")

# list1 = []
# i = 1 
# while i <= 10:
#     num = i ** 2
#     list1.append(num)
#     i += 1
# print(list1)

# list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0

# while index <= len(list2) - 1:
#     print(list2[index])
#     index += 1

# print("--------------------------------Question_4--------------------------------")

# tuple3 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# i = 0
# number = int(input("Enter the number you want to search for : "))

# while number in tuple3:
#     print(f"Found Number {number}...")
#     i += 1
#     break

# i = 0
# number = int(input("Enter the number you want to search for : "))
# while i < len(tuple3):
#     if (tuple3[i] == number):
#         print(f"Found Number {number} at index {i}")
#     i += 1
        
# print("--------------------------------Question_5--------------------------------")

# list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in list1:
#     print(i)
    
# print("--------------------------------Question_6--------------------------------")

# tuple2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
# num = int(input("Enter the number you are searching for : "))

# for i in range(0, len(tuple2)):
#     if (tuple2[i] == num):
#         print(f"Found {num} at index {i}")
        
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49

# idx = 0
# for el in tuple2:
#     if (el == x):
#         print(f"Found {x} at index {idx}")
#     idx += 1
        
# print("--------------------------------Question_7--------------------------------")

# for i in range(1, 101):
#     print(i)
    
# print("--------------------------------Question_8--------------------------------")

# for i in range(100, 0, -1):
#     print(i)
    
# print("--------------------------------Question_9--------------------------------")

# num = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# print("--------------------------------Question_10--------------------------------")

# n = int(input("Number : "))
# sum = 0
# i = 0
# while i <= n:
#     sum += i
#     i += 1
# print("Total Sum :", sum)

# print("--------------------------------Question_11--------------------------------")

# n = int(input("Number : "))
# i = 1
# factorial = 1

# for i in range(1, n + 1):
#     factorial = factorial * i
#     i += 1
# print(factorial)

