# from itertools import product

# elements_A = list(map(int, input().split()))
# print(" ".join(map(str, elements_A)))

# elements_B = list(map(int, input().split()))
# print(" ".join(map(str, elements_B)))

# cartesian_product = list(product(elements_A, elements_B))

# for i in cartesian_product:
#     print(i, end = " ")

# from itertools import permutations

# my_string = "ABCD"

# for i in sorted(permutations(my_string, 2)):
#     print(" ".join(i))

# Find the percentage

# def average(marks):
#     average_marks = sum(marks)/ len(marks)
#     return average_marks

# number_students = int(input("Enter the number of students : "))
# students = []

# for i in range(number_students):
#     student_input = input("Enter student name and marks : ")
#     data = student_input.split()
#     student_name = data[0]
#     student_marks = []
#     for mark in data[1:]:
#         student_marks.append(float(mark))
#     students.append((student_name, student_marks))

# name = input("Enter whose average you want to find : ")  
      
# for student_name, student_marks in students:
#     if name in student_name:
#         average_marks = average(student_marks)
#         print(f"{average_marks :.2f}")

# Average

# def average(array):
#     average_nums = sum(set(array))/ len(set(array))
#     return (f"{average_nums :.3f}")
   
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

# Symmetric Difference

# def difference(num1, num2):
#     set1 = set(num1)
#     set2 = set(num2)
#     result1 = set1.difference(set2)  
#     result2 = set2.difference(set1)
#     return result1, result2   

# size1 = int(input("Enter the size of the first set: "))
# arr1 = list(map(int, input("Enter elements for the first set: ").split()))

# size2 = int(input("Enter the size of the second set: "))
# arr2 = list(map(int, input("Enter elements for the second set: ").split()))

# result1, result2 = difference(arr1, arr2)

# result = []
# for i in result1:
#     result.append(i)
    
# for j in result2:
#     result.append(j)

# for i in sorted(result):    
#     print(i)

# Happiness Score calculation

# APPROACH 1 BASIC

# set_a = {1, 3, 4, 7, 2, 4, 7, 7}
# set_b = {8, 9, 33, 23, 89, 12, 23}

# happiness = 0
# limit = int(input("Enter the number of times you want to select a number : "))

# for i in range(0,limit):
#     input_num = int(input("Enter a number of ur choice : "))
#     if input_num in set_a:
#         happiness += 1
#         print("I am from set A")
#     elif input_num in set_b:
#         happiness -= 1
#         print("I am from set B")
#     else:
#         print("I am from nowhere")
#         pass
# print(f"The Happiness Score is : {happiness}")

# APPROACH 2 

# size_n, size_m = map(int, input("Enter the size of n and m sepated by space : ").split())
# array = list(map(int, input(f"Enter {size_n} elements separated by space : ").split()))

# A = set(map(int, input(f"Enter A of size {size_m}: ").split()))
# B = set(map(int, input(f"Enter B of size {size_m}: ").split()))

# happiness = 0

# for num in A:
#     if num in array:
#         happiness += 1
#         print("I am from set A", num)
#     else:
#         print("I am from nowhere", num)
        
# for num in B:        
#     if num in array:
#         happiness -= 1
#         print("I am from set B", num)
#     else:
#         print("I am from nowhere", num)

# print(f"The Happiness Score is : {happiness}")

# APPROACH 3
    
# size_n, size_m = map(int, input().split())
# array = list(map(int, input().split()))

# A = set(map(int, input().split()))
# B = set(map(int, input().split()))

# happiness = 0

# for i in array:
#     if i in A:
#         happiness+=1
#     elif(i in B):
#         happiness-=1
        
# print(happiness)

# Count number of Distinct Stamps

# count = int(input("Enter the number of stamps : "))
# result_stamps = []

# for i in range(count):
#     stamps = input(f"Enter the {i + 1} stamp : ")
#     result_stamps.append(stamps)
# print(len(set(result_stamps)))

# remove(), discard(), pop()

# num_int = int(input("Enter the number of intergers : "))
# list_int = set(map(int, input(f"Enter {num_int} integers : ").split()))

# commands = int(input("Enter the number of commands : "))

# list_int.pop()
# list_int.remove(9)
# list_int.discard(9)
# list_int.discard(8)
# list_int.remove(7)
# list_int.pop()
# list_int.discard(6)
# list_int.remove(5)
# list_int.pop()
# list_int.discard(5)

# print(sum(list_int))

num_int = int(input("Enter the number of intergers : "))
list_int = set(map(int, input(f"Enter {num_int} integers : ").split()))

commands = int(input("Enter the number of commands : "))

for i in range(commands):
    command = input("Enter the command : ").split()
    if command[0] == 'pop':
        list_int.pop()
    elif command[0] == 'remove':
        value = int(command[1])
        list_int.remove(value)
    elif command[0] == 'discard':
        value = int(command[1])
        list_int.discard(value)
        
print(sum(list_int))

    
