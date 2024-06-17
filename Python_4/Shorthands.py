#SHORTHAND IF ELSE STATEMENT

# marks = 80

# if marks == 90 or marks == 80  or marks == 95:
#     print("Good Job!")
# else:
#     print("Okay")

# if 80 in [90,80,85]:
#     print("Good Job!")

# marks = 80

# # if marks > 90:
# #     print("Excellent")
# # else:
# #     print("Good Job!")

# print("Excellent") if marks > 90 else print("Good Job!")

#LIST COMPREHENSION

# list1 = [50, 30, 20, 60, 20, 40]

# # a = []

# # for i in list1:
# #     a.append(i*2)
# # print(a)

# print([i*2 for i in list1])

#ENUMERATE FUNCTION

# list2 = [50, 30, 20, 60, 20, 40]

# # index = 0
# # for i in list2:
# #     print(index, i)
# #     index += 1
    
# for i in enumerate(list2):
#     print(i)

#Using _ operator

# num1 = 90_00_000
# num2 = 10_000

# print(f'{num1 + num2 :,}')

#Lambda Function

# # def square(x):
# #     return x*x
# # print(square(4))

# x = lambda x: x*x
# print(x(4))

#Using Zip function

# print("Amisha has scored 95 marks in Pyhton")
# print("Aarushi has scored 99 marks in Surgery")
# print("Sheila has scored 98 marks in Chemistry")
# print("Arun has scored 96 marks in Commerce")

# names = ["Amisha", "Aarushi", "Sheila", "Arun"]
# marks = [95, 99, 98, 96]
# subjects = ["Python", "Surgery", "Chemistry", "Commerce"]

# for name, mark, subject in zip(names, marks, subjects):
#     print("{} has scored {} marks in {}. ".format(name, mark, subject))
