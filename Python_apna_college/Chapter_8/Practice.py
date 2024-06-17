# print("--------------------------------Question_1--------------------------------")

# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
        
#     def marks_average(self):
#         sum = self.marks1 + self.marks2 + self.marks3
#         print("Hi", self.name, "Your Average score is :", sum/3)

# s1 = Student("Arjun", 99, 98, 97)
# s1.marks_average()

# s2 = Student("Karan", 96, 95, 94)
# s2.marks_average()

# print("---------------------------------Question_2--------------------------------")

# class Account:
#     def __init__(self, account_no, balance):
#         self.account = account_no
#         self.balance = balance
        
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited from account")
#         print("Amount Remaining :", self.get_balance())
        
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited to account")   
#         print("Amount Remaining :", self.get_balance())
        
#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(567845, 10000)
# print(acc1.balance, acc1.account)
# acc1.debit(5000)
# acc1.credit(2000)

# print("--------------------------------Question_3--------------------------------")

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return (22/7) * (self.radius ** 2)
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# print("-------------------------------Question_4---------------------------------")

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
    
#     def showDetails(self):
#         print("Role: " + str(self.role))
#         print("Department: " + str(self.department))
#         print("Salary: " + str(self.salary))

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")
    
#     def showDetails(self):
#         super().showDetails()
#         print("Name: " + str(self.name))
#         print("Age: " + str(self.age))

# # e1 = Employee("Accountant", "Finance", "60,000")
# # e1.showDetails()
        
# e2 = Engineer("Ram", 40)
# e2.showDetails()        

# print("--------------------------------Question_5--------------------------------")

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
        
#     def __gt__(self, odr2):
#         return self.price > odr2.price 
        
# odr1 = Order("Chips", 20)
# odr2 = Order("Tea", 15)

# print(odr1 > odr2)
