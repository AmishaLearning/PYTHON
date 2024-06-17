# List Programs Part 1

# # Python program to interchange first and last elements in a list
# list1 = [1, 2, 5, 7, 90, 56]
# list1[0], list1[-1] = list1[-1], list1[0]
# print(list1)

# # Python program to swap two elements in a list

# list2 = [12, 34, 45, 56, 67, 78, 89, 23]

# i = int(input("Enter the First element's index which you want to swap : "))
# j = int(input("Enter the Second element's index which you want to swap : "))

# print(f"List Before Swapping : {list2}" )
# list2[i], list2[j] = list2[j], list2[i]
# print(f"List After Swapping  : {list2}" )

# # Python – Swap elements in String list

# string1 = ["Voilet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]

# print(f"The original string is                     : {string1}")

# for i in range(len(string1)):
#     string1[i] = string1[i].replace("i", "A")
#     string1[i] = string1[i].replace("e", "Z")

# print(f"The string after replacing 'i' with 'A' is : {string1}")

# # Python | Ways to find length of list

# list3 = [12, 23, 34, 45, 56, 67, 78, 89, 15, 26, 37, 48, 59]
# count = 0
# print(f"The length of the list is             : {len(list3)}")

# for i in list3:
#     count = count + 1
    
# print(f"The length of the list using count is : {count}")

# # Maximum and Minimum of two numbers

# num1 = int(input("Enter the First number  : "))
# num2 = int(input("Enter the Second number : "))

# if num1 > num2 :
#     print(f"{num1} is Maximum")
# else:
#     print(f"{num2} is Maximum")
    
# if num1 < num2 :
#     print(f"{num1} is Minimum")
# else:
#     print(f"{num2} is Minimum")
    
# # Python | Ways to check if element exists in list

# string2 = ["VOILET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"]
# print(f"The list is : {string2}")

# check = input("Enter the element you want to check : ")
# check_status = check.upper()

# if check_status in string2:
#     print(f"Yes! The element {check_status} is present in the String")
# else:
#     print(f"No! The element {check_status} is not present in the String")

# # for i in string2:
# #     if (i == check_status):
# #         print(f"Yes! The element {check_status} is present in the String")
# #     else: 
# #         print(f"No! The element {check_status} is not present in the String")

# Different ways to clear a list in Python

# list4 = ["Stone", "Paper", "Scissors", "Snake", "Water", "Gun"]

# # while list4:
# #     list4.pop()
    
# # print(list4)

# list4.clear()
# print(list4)

# # Python | Reversing a List

# list5 = ["Stone", "Paper", "Scissors", "Snake", "Water", "Gun"]
# print(list5[::-1])

# Python | Cloning or Copying a list

# list6 = ["Stone", "Paper", "Scissors", "Snake", "Water", "Gun"]
# list7 = []
# for i in list6:
#     list7.append(i)
    
# print(list7)

# def copy(list6):
#     list7 = []
#     list7.extend(list6)
#     return list7

# list6 = ["Stone", "Paper", "Scissors", "Snake", "Water", "Gun"]

# print(copy(list6))


