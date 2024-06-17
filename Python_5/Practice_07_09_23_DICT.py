# Python | Sort Python Dictionaries by Key or Value

# dict1 = {"Apple" : 18, "Mango" : 12, "Banana" : 11, "Grapes" : 19, "Pomegranate" : 5}
# list1 = dict(sorted(dict1.items()))
# print(list1)

# dict1 = {"Apple" : 18, "Mango" : 12, "Banana" : 11, "Grapes" : 19, "Pomegranate" : 5}
# # dict1 = {12 : 21, 32 : 23, 14 : 41, 99 : 5}

# print("----------------------------------------------------------------------------------------------------")
# print("Sorting using dict1.items()")
# list1 = list(dict1.items())
# print(f"Before Sorting : {list1}")
# list1.sort()
# print(f"After Sorting  : {list1}")
# print("----------------------------------------------------------------------------------------------------")

# print("Sorting using dict1.values()")
# list1 = list(dict1.values())
# print(f"Before Sorting : {list1}")
# list1.sort()
# print(f"After Sorting  : {list1}")
# print("----------------------------------------------------------------------------------------------------")

# print("Sorting using dict1.keys()")
# list1 = list(dict1.keys())
# print(f"Before Sorting : {list1}")
# list1.sort()
# print(f"After Sorting  : {list1}")
# print("----------------------------------------------------------------------------------------------------")

# Handling missing keys in Python dictionaries

# elements = {"a" : 5, "c" : 8, "d" : 2}
# if "b" in elements:
#     print(elements["b"])
# else:
#     print("Element Not Found")

# Python dictionary with keys having multiple inputs

# multikey_dict = {('Apple', 'Mango'): 30, ('Banana', 'Orange'): 25, ('Pomegranate', 'Grapes'): 35}
# print(multikey_dict.keys())  

# Python program to find the sum of all items in a dictionary

# dict2 = {('Apple', 'Mango'): 30, ('Banana', 'Orange'): 25, ('Pomegranate', 'Grapes'): 35}
# print(sum(dict2.values()))

# Python program to find the lenght of a Dictionary

# dict3 = {"Apple" : 18, "Mango" : 12, "Banana" : 11, "Grapes" : 19, "Pomegranate" : 5}
# print(len(dict3.keys()))

# Ways to sort list of dictionaries by values in Python – Using itemgetter

# from operator import itemgetter

# list1 = [{"Fruit" : "Apple", "Quantity" : 20 },
#          {"Fruit" : "Bnana", "Quantity" : 25 },
#          {"Fruit" : "Grapes", "Quantity" : 19 }]

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Quantity : ")
# print(sorted(list1, key = itemgetter('Quantity')))

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Quantity and Fruit : ")
# print(sorted(list1, key = itemgetter('Quantity', 'Fruit')))

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Fruit and Quantity : ")
# print(sorted(list1, key = itemgetter('Fruit', 'Quantity')))

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Quantity in Descending Order : ")
# print(sorted(list1, key = itemgetter('Quantity'), reverse = True))

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Fruit in Descending Order : ")
# print(sorted(list1, key = itemgetter('Fruit'), reverse = True))

# print("---------------------------------------------------------------------------------------------------------------")

# Ways to sort list of dictionaries by values in Python – Using lambda function

# list1 = [{"Fruit" : "Apple", "Quantity" : 20 },
#          {"Fruit" : "Bnana", "Quantity" : 25 },
#          {"Fruit" : "Grapes", "Quantity" : 19 }]

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Quantity : ")
# print(sorted(list1, key = lambda i : i['Quantity']))

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Quantity and Fruit : ")
# print(sorted(list1, key = lambda i : (i['Quantity'], i['Fruit'])))

# print("---------------------------------------------------------------------------------------------------------------")

# print("The List printed sorting by Fruit and Quantity : ")
# print(sorted(list1, key = lambda i : (i['Fruit'], i['Quantity'])))

# print("---------------------------------------------------------------------------------------------------------------")

# Python | Merging two Dictionaries

# dict2 = {"Fruit" : "Apple", "Quantity" : 20 }
# dict3 = {"Fruit" : "Banana" , "Quantity" : 27}

# # list2 = list(dict2.values())
# # list3 = list(dict3.values())

# # list2.extend(list3)

# # print(list2)

# dict2.update(dict3)
# print(dict2)

# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}

# dict2.update(dict1)

# print(dict2)
        
# Program to create grade calculator in Python

harry = {"name"        : "Harry Potter",
         "assignment"  : [80, 50, 40, 20],
         "test"        : [75, 75],
         "lab"         : [78.20, 77,20]}

hermoine = {"name"        : "Hermoine Granger",
            "assignment"  : [82, 56, 44, 30],
            "test"        : [80, 80],
            "lab"         : [67.90, 78,72]}

ron = {"name"        : "Ronald Weasley",
       "assignment"  : [77, 82, 23, 39],
       "test"        : [78, 77],
       "lab"         : [80, 80]}

diggory = {"name"      : "Cedric Diggory",
         "assignment"  : [67, 55, 77, 21],
         "test"        : [40, 50],
         "lab"         : [69, 44.56]}

ginny = {"name"        : "Ginny Weasley",
         "assignment"  : [29, 89, 60, 56],
         "test"        : [65, 56],
         "lab"         : [50, 40.6]}

def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum/ len(marks)

def calculate_total_average(students):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
    lab = get_average(students["lab"])
    
    return(0.1 * assignment + 0.7 * test + 0.2 * lab)

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"    
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"
    
def class_average(student_list):
    result_list = []
    
    for students in student_list:
        stud_avg = calculate_total_average(students)
        result_list.append(stud_avg)
        return get_average(result_list)
    
students = [harry, hermoine, ron, diggory, ginny]

for i in students:
    print("------------------------------------------------------------------")
    print()
    print(i['name'])
    print(f"Average marks of {i['name']} is : {calculate_total_average(i)}")
    print(f"Grade of {i['name']} is : {assign_grade(calculate_total_average(i))}")
    print()
    
class_av = class_average(students)

print("------------------------------------------------------------------")
print(f"Class Average is : {class_av}")
print(f"Grade of class is : {assign_grade(class_av)}")