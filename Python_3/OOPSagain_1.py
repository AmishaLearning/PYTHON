# class Employee:
#     pass

# emp_1=Employee()
# emp_2=Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Max'
# emp_1.last = 'Well'
# emp_1.email = 'max.well@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Jonathan'
# emp_2.last = 'Wills'
# emp_2.email = 'jonathan.wills@company.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)

#USING INIT FUNCTION

class Employee:
    def __init__(self,first,last,pay):#Constructor/instance
        #objects need not to be same as arguments(left 'first' is object...right 'first' is argument
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self):
        return '{} {} '.format(self.first,self.last)
                

emp_1=Employee('Max','Well',50000)#__init__ method runs automatically
emp_2=Employee('Jonathan','Wills',60000)

# print(emp_1)
# print(emp_2)


#print(emp_1.fullname)#prints method instead of value
# print(emp_1.fullname())
# print(emp_2.fullname())

emp_1.fullname()
print(Employee.fullname(emp_1))