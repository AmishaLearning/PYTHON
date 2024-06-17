# SINGLE INHERITANCE

# class Parent:
#     def func1(self):
#         print("This function is in Parent class")

# class Child(Parent):
#     def func2(self):
#         print("This function is in Child Class")
        
# object = Child()
# object.func1()
# object.func2()

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
#         print(f"Father : {self.fathername}")
#         print(f"Father : {self.mothername}")
        
# s1 = Son()
# s1.fathername = "Ram"
# s1.mothername = "Sita"
# s1.parents()

# class Mother:
#     def __init__(self, mother):
#         self.mother = mother

# class Father:
#     def __init__(self, father):
#         self.father = father 
        
# class Son(Mother, Father):
#     def __init__(self):
#         Mother.__init__(self, "Sita")
#         Father.__init__(self, "Ram")
        
#     def display(self):
#         print(self.mother, self.father)

# object = Son()
# object.display()

# MULTILEVEL INHERITANCE

# class GrandFather:
    
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
        
# class Father:
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
        
#         GrandFather.__init__(self, grandfathername)

# class Son(Father):
#     def __init__(self, sonname,  fathername, grandfathername):
#         self.sonname = sonname
        
#         Father.__init__(self, fathername, grandfathername)
        
#     def print_name(self):
#         print("Grandfather name : ", self.grandfathername)
#         print("Father Name      : ", self.fathername)
#         print("Son Name         : ", self.sonname)
        
# s1 = Son("Prince", "King", "SuperKing")
# print(s1.grandfathername)
# s1.print_name()

# HIERARCHICAL INHERITANCE

# class Parent:
#     def func1(self):
#         print("This Function is in Parent class")
        
# class Child1(Parent):
#     def func2(self):
#         print("This function is from child 1")

# class Child2(Parent):
#     def func3(self):
#         print("This function is from child 2")

# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()

# HYBRID INHERITANCE

# class School:
#     def func1(self):
#         print("This function is in School")

# class Student1(School):
#     def func2(self):
#         print("This function is in Student 1")

# class Student2(School):
#     def func3(self):
#         print("This function is in Student 2")

# class Student3(Student1, School):
#     def func4(self):
#         print("This function is from Student 3")

# object = Student3()
# object.func1()
# object.func2()    
# object.func4()

# PROTECTED MEMBERS

# class Base:
#     def __init__(self):
#         self._a = 2
        
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling Protected member of the base class : ", self._a)
        
#         self._a = 3
#         print("Calling protected member outside class : ", self._a)
        
# obj1 = Derived()
# obj2 = Base()

# print("Accessing protected member of obj1 : ", obj1._a)
# print("Accessing protected member of obj2 : ", obj2._a)

# PRIVATE MEMBERS

# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "Geeksfor Geeks"

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class : ")
#         print(self.__c)

# obj1 = Base()
# print(obj1.a)

# Uncommenting print(obj1.c) will raise an AttributeError
# print(obj1.c)

# Uncommenting obj2 = Derived() will also raise an AttributeError as
# private member of base class is called inside derived class

# obj2 = Derived()

# POLYMORPHISM

# class India:
#     def capital(self):
#         print("New Delhi is the capital of India.")
    
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
        
#     def type(self):
#         print("India is a developing Country.")

# class USA:
#     def capital(self):
#         print("Washington, D.C. is the capital of U.S.A")
    
#     def language(self):
#         print("English is the primary language of USA")
    
#     def type(self):
#         print("USA is a Developed Country.")

# obj_ind = India()
# obj_usa = USA()

# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

# METHOD OVERRIDING

# class Bird:
#     def intro(self):
#         print("I am from class Bird")
#         print("There are many types of Birds.")
    
#     def flight(self):
#         print("I am from class Bird")
#         print("Most of the birds can fly but some cannot.")
    
# class sparrow(Bird):
#     def flight(self):
#         print("I am from class Sparrow")
#         print("Sparrows can fly")
    
# class ostrich(Bird):
#     def flight(self):
#         print("I am from class Ostrich")
#         print("Ostriches cannot fly")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()

# Implementing Polymorphism with a Function 

# class India():
# 	def capital(self):
# 		print("New Delhi is the capital of India.")

# 	def language(self):
# 		print("Hindi is the most widely spoken language of India.")

# 	def type(self):
# 		print("India is a developing country.")

# class USA():
# 	def capital(self):
# 		print("Washington, D.C. is the capital of USA.")

# 	def language(self):
# 		print("English is the primary language of USA.")

# 	def type(self):
# 		print("USA is a developed country.")

# def func(obj):
# 	obj.capital()
# 	obj.language()
# 	obj.type()

# obj_ind = India()
# obj_usa = USA()

# func(obj_ind)
# func(obj_usa)

# Polymorphism in Python using inheritance and method overriding:

# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!!"

# animals = [Dog(), Cat()]

# for animal in animals:
#     print(animal.speak())    

# Class or Static Variables in Python

# class CSStudent:
#     stream = "CSE"          # Class variable
#     def __init__(self, name, roll) :
#         self.name = name    # Instance Variable
#         self.roll = roll    # Instance Variable
        
# a = CSStudent("Geek", 1)
# b = CSStudent("Nerd", 2)      

# print(a.stream)
# print(b.stream)
# print(a.name)
# print(b.name)
# print(a.roll)
# print(b.roll)

# print(CSStudent.stream)  
    
# a.stream = "ECE"
# print(a.stream)
# print(b.stream)

# CSStudent.stream = "MECH"

# print(a.stream)
# print(b.stream)

# class MyClass:
# 	static_var = 0

# 	def __init__(self):
# 		MyClass.static_var += 1
# 		self.instance_var = MyClass.static_var

# obj1 = MyClass()
# print(obj1.instance_var) # Output: 1

# obj2 = MyClass()
# print(obj2.instance_var) # Output: 2

# obj3 = MyClass()
# print(obj3.instance_var)

# print(MyClass.static_var) # Output: 2


# CLASS METHOD

# class Myclass:
#     def __init__(self, value):
#         self.value = value
    
#     def getValue(self):
#         return self.value
    

# obj = Myclass(10)

# print(obj.getValue())

# STATIC METHOD

# class Myclass:
#     def __init__(self, Value):
#         self.value = Value
        
#     @staticmethod
#     def get_max_value(x, y):
#         return max(x, y)
    
# obj = Myclass(10)
# print(Myclass.get_max_value(20, 30))
# print(obj.get_max_value(20, 30))

# class method and static method.

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def isAdult(age):
        return age > 18
    
person1 = Person("Mayank", 21)
person2 = Person.fromBirthYear("Mayank", 1996)

print(person1.age)
print(person2.age)

print(Person.isAdult(22))