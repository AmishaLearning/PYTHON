# class Addition:
#     first = 0
#     second = 0
#     answer = 0
    
#     def __init__(self, f, s):
#         self.first = f
#         self.second = s
        
#     def display(self):
#         print(f"First number is : {self.first}")
#         print(f"Seconf number is : {self.second}")
#         print(f"Addition of two number is : {self.answer}")
    
#     def calculate(self):
#         self.answer = self.first + self.second
        
# obj1 = Addition(1000, 2000)
# obj2 = Addition(10, 20)

# obj1.calculate()
# obj2.calculate()

# obj1.display()
# obj2.display()

# CONSTRUCTOR

# class Myclass:
#     def __init__(self, name = None):
#         if name is None:
#             print("Default Constructor is called")
#         else:
#             self.name = name
#             print(f"Parameterized Constructor is called with name : {self.name}")
    
#     def method(self):
#         if hasattr(self, 'name'):
#             print(f"Method called with name : {self.name}")
#         else:
#             print("Method called without a name")
            
# obj1 = Myclass()
# obj1.method()
# obj2 = Myclass("John")
# obj2.method()

# DESTRUCTOR

# class Employee:
    
#     def __init__(self):
#         print("Employee created.")
    
#     def __del__(self):
#         print("Destructor called, Employee deleted.")
# obj = Employee()
# del obj

# class Employee:
    
#     def __init__(self):
#         print("Employee Created")
        
#     def __del__(self):
#         print("Destructor called")

# def Create_obj():
#     print("Making Object...")
#     obj = Employee()
#     print("Function end...")
#     return obj

# print("Calling Create_obj() Function...")
# obj = Create_obj()
# print("Program End")

# class A:
#     def __init__(self, bb):
#         self.b = bb
#         print("I am from class A")

# class B:
#     def __init__(self): 
#         self.a = A(self)
#         print("I am from class B")
#     def __del__(self):
#         print("Die")

# def fun():
#     b = B()
    
# fun()       

# Destruction in recursion

# class RecursiveFunction:
#     def __init__(self, n):
#         self.n = n
#         print(f"Recursive Function initialized with n = {n}")
    
#     def run(self, n = None):
#         if n is None:
#             n = self.n
#         if n <= 0:
#             return
#         print(f"Running recursive function with n = {n}")
#         self.run(n - 1)
    
#     def __del__(self):
#         print("Recursive Function Object Destroyed")
        
# obj = RecursiveFunction(5)
# obj.run()
# del obj

# INHERITANCE

# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
    
#     def Display(self):
#         print(self.name, self.id)
        
# emp = Person("Satyam", 102)
# emp.Display()

# class Emp(Person):
#     def Print(self):
#         print("Emp class Called")
        
# Emp_details = Emp("Mayank", 103)
# Emp_details.Display()
# Emp_details.Print()

# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def getName(self):
#         print("I am from class Person")
#         return self.name
    
#     def isEmployee(self):
#         print("I am from class Person")
#         return False

# class Employee(Person):
    
#     def isEmployee(self):
#         print("I am from class Employee")
#         return True
    
# emp = Person("Geek1")
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Geek2")
# print(emp.getName(), emp.isEmployee())

# class Person:
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
        
#     def Display(self):
#         print(self.name)
#         print(self.idnumber)

# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
    
#         Person.__init__(self, name, idnumber)

# a = Employee("Jin", 12345, 1200000, "Intern")
# a.Display()

# b = Person("Amit", 54321)
# b.Display()
        
# Python program to demonstrate error if we forget to invoke __init__() of the parent

# class A:
#     def __init__(self, n = "Shaan"):
#         self.name = n

# class B(A):
#     def __init__(self, roll):
#         self.roll = roll
        
# object = B(23)
# print(object.name)
# print(object.roll)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)
        
# class Student(Person):
#     def __init__(self, name, age):
#         self.sname = name
#         self.sage = age
        
#         super().__init__("Ananad", age)
        
#     def displayInfo(self):
#         print(self.sname, self.sage)
            
# obj = Student("Mayank", 23)
# obj.display()
# obj.displayInfo()

# Adding Properties

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print(self.name, self.age)
        
# class Student(Person):
#     def __init__(self, name, age, dob):
#         self.sname = name
#         self.sage = age
#         self.dob = dob
        
#         super().__init__("Ananad", age)
        
#     def displayInfo(self):
#         print(self.sname, self.sage, self.dob)
            
# obj = Student("Mayank", 23, "16-02-2000")
# obj.display()
# obj.displayInfo()

# MULTIPLE INHERITANCE

class Base1:
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
    
class Base2:
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
        
class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    
    def printStrs(self):
        print(self.str1, self.str2)

object = Derived()
object.printStrs()

# MULTILEVEL INHERITANCE

# class Base:
    
#     def __init__(self, name):
#         self.name = name
        
#     def getName(self):
#         return self.name

# class Child(Base):
    
#     def __init__(self, name, age):
#         Base.__init__(self, name)   
#         self.age = age
        
#     def getAge(self):
#         return self.age
    
# class GrandChild(Child):
    
#     def __init__(self, name, age, address):
#         Child.__init__(self, name, age)
#         self.address = address
        
#     def getAddress(self):
#         return self.address
    

# g = GrandChild("QWERTY", 12, "Noida")
# print(g.getName(), g.getAge(), g.getAddress())

# Private members of the parent class 

# class C:
#     def __init__(self):
#         self.c = 21
#         self.__d = 42
       
# class D(C):
#     def __init__(self):
#         self.e = 82
#         C.__init__(self)

# object = D()
# print(object.c)
# print(object.__d)



        