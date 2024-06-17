#Regular methods in a class automatically take the instance as the first argument (self in our case) 

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
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
                     
print("Number of Employees : ", Employee.num_of_emps) 
               
emp_1=Employee('Max','Well',50000)
emp_2=Employee('Jonathan','Wills',60000)

Employee.set_raise_amt(1.09)#working with class instead of the instance

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)