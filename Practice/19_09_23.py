# Incorrect Regex 
# import re
# test_num = int(input("Enter the number of test cases : "))
# for i in range(test_num):
#     case = input("Enter the string : ")   
#     try:
#         re.compile(case)
#         print(True)
#     except re.error:
#         print(False)

# DefaultDict Tutorial -- For 1 case
# group_size = list(map(int, input("Enter the value of n and m : ").split()))
# elements_A = []
# elements_B = []

# for i in range(group_size[0]):
#     group_A = input(f"Enter {i + 1} element of A : ")
#     elements_A.append(group_A)
# print(elements_A)

# for j in range(group_size[1]):
#     group_B = input(f"Enter {j + 1} element of B : ")
#     elements_B.append(group_B)
# print(elements_B)

# indexes_a = [] 
# indexes_b = []

# for i, element in enumerate(elements_A, start = 1):
#     if element == 'a':
#         indexes_a.append(i)
#     elif element == 'b':
#         indexes_b.append(i)

# print(" ".join(map(str,indexes_a)))
# print(" ".join(map(str,indexes_b)))

# n, m = map(int, input("Enter the value of n and m: ").split())

# word_index_map = {}

# for i in range(n):
#     word = input(f"Enter word {i + 1} of group A: ")
#     if word in word_index_map:
#         word_index_map[word].append(i + 1)
#     else:
#         word_index_map[word] = [i + 1]

# for j in range(m):
#     word_B = input(f"Enter word {j + 1} of group B: ")
    
#     if word_B in word_index_map:
#         indices = word_index_map[word_B]
#         print(" ".join(map(str, indices)))
#     else:
#         print(-1)

# Collections.namedtuple()

# from collections import namedtuple

# Point = namedtuple('Point', 'x, y')
# pt1 = Point(1, 2)
# pt2 = Point(3, 4)
# dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# print(dot_product)

# Car = namedtuple('Car', 'Price Mileage Color Class')
# xyz = Car(Price = 100000, Mileage = 30, Color = 'Cyan', Class = 'Y')
# print(xyz)
# print(xyz.Class)
# from collections import namedtuple

# AVERAGE

# students = int(input("Enter the number of Students: "))
# column_names = input("Enter the Column names: ").split()
# Columns = namedtuple('Columns', column_names)
# student_data = []

# for i in range(students):
#     data = input(f"Enter data for student {i + 1}: ").split()
#     IDS, MARKS, NAME, CLASS = map(str, data[0:4])
#     student = Columns(int(IDS), int(MARKS), NAME, CLASS)

#     student_data.append(student)

# total_marks = 0

# for student in student_data:
#     total_marks += student.MARKS

# average = total_marks / students

# print(f"Average Marks: {average:.2f}")

# from collections import namedtuple

# students = int(input("Enter the number of Students: "))
# column_names = input("Enter the Column names (space-separated): ").split()
# Columns = namedtuple('Columns', column_names)
# student_data = []

# for i in range(students):
#     data = input(f"Enter data for student {i + 1}: ").split()
#     if len(data) == len(column_names):
#         student = Columns(*data)  
#         student_data.append(student)

# total_marks = 0

# for student in student_data:
#     total_marks += int(student.marks)

# average = total_marks / students

# print(f"Average Marks: {average:.2f}")

# Validating phone number

num_input = int(input("Enter the count of phone numbers : "))

for i in range(num_input):
    number = input("Enter the number : ")
    
    if number.isdigit() == True and len(number) == 10 and number[0] in ['7', '8', '9']:
        print("YES")
    else:
        print("NO")
            