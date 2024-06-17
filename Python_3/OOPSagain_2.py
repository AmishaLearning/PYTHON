#Class variables are shared among all the instances of a class
#instance variables are unique for the instances like name, pay, email
#Class variables should be same for each instances

# class Employee:
    
#     raise_amount = 1.04
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@company.com"
        
#     def fullname(self):
#         return '{} {} '.format(self.first,self.last)
    
#     def apply_raise(self):
#         self.pay = int((self.pay * self.raise_amount))
#         # self.pay = int((self.pay * Employee.raise_amount))                
               
# emp_1=Employee('Max','Well',50000)#__init__ method runs automatically
# emp_2=Employee('Jonathan','Wills',60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount 
# Employee.raise_amount

# class Employee:
    
#     raise_amount = 1.04
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@company.com"
        
#     def fullname(self):
#         return '{} {} '.format(self.first,self.last)
    
#     def apply_raise(self):
#         self.pay = int((self.pay * self.raise_amount))
#         # self.pay = int((self.pay * Employee.raise_amount))                
               
# emp_1=Employee('Max','Well',50000)#__init__ method runs automatically
# emp_2=Employee('Jonathan','Wills',60000)

# #printing namespace of employee 1
# # print(Employee.__dict__)

# # Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps +=1
        
    def fullname(self):
        return '{} {} '.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int((self.pay * self.raise_amount))
                     
print("Number of Employees : ", Employee.num_of_emps) 
               
emp_1=Employee('Max','Well',50000)
emp_2=Employee('Jonathan','Wills',60000)

print("Number of Employees : ", Employee.num_of_emps) 
