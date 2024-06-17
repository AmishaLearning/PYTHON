#SHORTHAND IFELSE

# a = 330
# b = 3303
# print("A") if a > b else print("=") if a == b else print("B")

# c = 9 if a < b else ""
# print(c)

#Enumerate function  

# marks = [12, 56, 23, 45 ,67 ,89, 48, 80]
# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Good")
#     index = index + 1

# Enumerate function gives index of list alongwith the values
# marks = [12, 56, 23, 45 ,67 ,89, 48, 80]

# for index, mark in enumerate(marks):
#     print(mark)
#     if (index == 3):
#         print("Good")
    
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes", "Pomegranate"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print("--------------")
    
for index, fruit in enumerate(fruits):
    print(index, fruit)