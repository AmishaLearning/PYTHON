# print("-----------------------------Class/Object --------------------------------")

# class Student:
#     name = "karan"
    
# s1 = Student()
# print(s1)
# print(s1.name) 

# s2 = Student()
# print(s2.name) 

# class Car:
#     color = "Blue"
#     brand = "Mrecedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# print("-----------------------------init-----------------------------")

# class Employee:
#     def __init__(self):
#         print("I am an Employee class")
# s2 = Employee()

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("Adding a nnew student in database")
        
# s1 = Student("Karan")
# print(s1.name)

# class Student:
#     college_name = "ABC College"
#     name = "Anonymous"
    
#     def __init__(self,name):
#         self.name = name
#         print("Adding a nnew student in database")
        
# s1 = Student("Karan")
# print(s1.name)

# print("-------------------------------Methos-------------------------------")

# class Student:
#     college_name = "ABC College"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome Student", self.name)
    
#     def get_marks(self):
#         return self.marks
    
# s1 = Student("Karan", 89)
# s1.welcome()
# print(s1.get_marks())

# print("--------------------------------Static Methods--------------------------------")

# class Student:
#     @staticmethod # decorator 
#     def college():
#         print("ABC College")
# s1 = Student()
# s1.college()

print("--------------------------Abstraction--------------------------------")

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

car1 = Car()
car1.start()  