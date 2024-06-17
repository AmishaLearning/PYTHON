# DESTRUCTORS

# class Employee:
#     def __init__(self):
#         print("Employee Created")
    
#     def __del__(self):
#         print("Destructor called, Employee deleted")

# obj = Employee()
# del obj

# class Employee:
#     def __init__(self):
#         print("Employee Created")
#     def __del__(self):
#         print("Destructor Called")

# def Create_obj():
#     print("Making Object...")
#     obj = Employee()
#     print("Function End...")
#     return obj

# print("Calling Create_obj() function")
# obj = Create_obj()
# print("Program End")

# class A:
#     def __init__(self, bb):
#         self.b = bb
    
# class B:
#     def __init__(self):
#         self.a = A(self)
#     def __del__(self):
#         print("die")

# def fun():
#     b = B()
# fun()
        
# INHERITANCE

# Creating Parent Class and Child Class
# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def display(self):
#         print(self.name, self.id)
        
# emp = Person("Satyam", 102)
# emp.display()

# class Emp(Person):
#     def print(self):
#         print("Emp Class called")

# Emp_details = Emp("Mayank", 103)
# Emp_details.display()
# Emp_details.print()

# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def getName(self):
#         return self.name

#     def isEmployee(self):
#         return False

# class Employee(Person):
#     def isEmployee(self):
#         return True
    
# Emp = Person("Geek1")
# print(Emp.getName(), Emp.isEmployee())

# Emp = Employee("Geek2")
# print(Emp.getName(), Emp.isEmployee())

# super()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print(self.name, self.age)
        
# class Student(Person):
#     def __init__(self, name, age):
#         self.sName = name
#         self.sAge = age
    
#         super().__init__("Nikhil", 24)
        
#     def displayInfo(self):
#         print(self.sName, self.sAge)

# obj = Student("Mayank", 23)
# obj.display()
# obj.displayInfo()

# Adding New Properties

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name, self.age)
        
# class Student(Person):
#     def __init__(self, name, age, dob):
#         self.sName = name
#         self.sAge = age
#         self.dob = dob
#         super().__init__("Ram", age)
        
#     def displayInfo(self):
#         print(self.sName, self.sAge, self.dob)

# obj = Student("Shyam", 27, "16-03-1996")
# obj.display()
# obj.displayInfo()

# SINGLE INHERITANCE

# class Parent:
#     def func1(self):
#         print("This function is from Parent Class")

# class Child(Parent):
#     def func2(self):
#         print("This function is from Child class")
        
# obj = Child()
# obj.func1()
# obj.func2()

# MULTIPLE INHERITANCE

# class Mother:
#     mothername = ""
#     def mother(self):
#         print(self.mothername)

# class Father:
#     fathername = ""
#     def father(self):
#         print(self.fathername)
        
# class Son(Mother, Father):
#     def parents(self):
#         print("Father : ", self.fathername)
#         print("Mother : ", self.mothername)
        
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()

# MULTILEVEL INHERITANCE

# class Grandfather:
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
        
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         Grandfather.__init__(self, grandfathername)

# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         Father.__init__(self, fathername, grandfathername)
        
#     def print_name(self):
#         print("Grand Father : ", self.grandfathername)
#         print("Father       : ", self.fathername)
#         print("Son          : ", self.sonname)
        
# obj = Son("SbJr. Arjun", "Jr. Arjun", "Sr. Arjun")
# obj.print_name()

# HIERARCHICAL INHERITANCE

# class Parent:
#     def func1(self):
#         print("This function is in Parent Class")

# class Child1(Parent):
#     def func2(self):
#         print("This is from Child class 1") 
        
# class Child2(Parent):
#     def func3(self):
#         print("This is from Child class 2")

# obj1 = Child1()
# obj2 = Child2()
# obj1.func1()
# obj1.func2()
# obj2.func1()
# obj2.func3()


   
        
        