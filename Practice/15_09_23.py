# LEET CODE
# Two sum

# list1 = list(map(int, input("Enter the elements of the list : ").split()))
# target = int(input("Enter the target value : "))

# found = False  

# for i in range(len(list1)):  
#     for j in range(i + 1, len(list1)):  
#         if list1[i] + list1[j] == target:
#             found = True
#             break  
#     if found:
#         print([list1[i], list1[j]])
#         break  
# else:
#     print("Not Found")

# Hacker rank Again 

# Zipped!....Average 

# students, subjects = map(int, input("Enter no. of students and no. of subjects : ").split())
# grades = []


# for i in range(subjects):
#     student_marks = list(map(float, input("Enter the marks : ").split()))
#     grades.append(student_marks)
    
# for i in range(subjects):
#     total_score = 0
#     for j in range(students):
#         total_score += grades[i][j]
#     average = total_score / subjects
#     print(f"Avearge for {i} student : {average :.1f}")

# Input
n, m = map(int, input().split())  # n is the number of students, m is the number of subjects
grades = []

# Read grades
for _ in range(n):
    student_grades = list(map(float, input().split()))
    grades.append(student_grades)

# Calculate averages and print them with one decimal place
for j in range(m):
    total_score = 0
    for i in range(n):
        total_score += grades[i][j]
    
    average = total_score / n
    print(f"{average:.1f}")


   