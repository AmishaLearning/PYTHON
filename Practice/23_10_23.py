# Class and Objects

# class Dog:
#     attr1 = "Mammal"
    
#     def __init__(self, name):
#         self.name = name
        
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")

# print("Roger is a {}".format(Dog.attr1))
# print("Tommy is a {}".format(Tommy.__class__.attr1))

# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))

# class Dog:
#     attr1 = "Mammal"
    
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print("My nam is {}".format(self.name))

# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")

# Rodger.speak()
# Tommy.speak()

# Python Inheritance

# Single Inheritance

# class Person:
    
#     def __init__(self, name, idnumber):
#         print("I am from Class Person __init__")
#         self.name = name
#         self.idnumber = idnumber
    
#     def display(self):
#         print("I am from Class Person display")
#         print(self.name)
#         print(self.idnumber)
        
#     def details(self):
#         print("I am from Class Person details")
#         print("My name   : {}".format(self.name))
#         print("Id number : {}".format(self.idnumber))

        
# class Employee(Person):
    
#     def __init__(self, name, idnumber, salary, post):
#         print("I am from Class Employee __init__")
#         self.salary = salary
#         self.post = post
#         Person.__init__(self, name, idnumber)
        
#     def details(self):
#         print("I am from Class Employee details")
#         print("My name   : {}".format(self.name))
#         print("Id number : {}".format(self.idnumber))
#         print("Post      : {}".format(self.post))
        

# Emp = Employee("Ram", 43215, 67890, "Intern")
# Emp1 = Person("Shyam", 98765)

# Emp.display()
# Emp.details()

# Emp1.display()
# Emp1.details()
        
# Polymorphism

# class Bird:
#     def intro(self):
#         print("I am from class Bird intro")
#         print("There are many types of Birds")
#         print()
        
#     def flight(self):
#         print("I am from class Bird flight")
#         print("Most of the birds can fly but some cannot")
#         print()
        
# class sparrow(Bird):
#     def flight(self):
#         print("I am from class Sparrow")
#         print("Sparrow can Fly")
#         print()
        
# class ostrich(Bird):
#     def flight(self):
#         print("I am from class Ostrich")
#         print("Ostriches cannot Fly")
#         print()
        
# obj_Bird = Bird()
# obj_sparrow = sparrow()
# obj_ostrich = ostrich()

# obj_Bird.intro()
# obj_Bird.flight()

# obj_sparrow.intro()
# obj_sparrow.flight()

# obj_ostrich.intro()
# obj_ostrich.flight()
        
# Encapsulation

# class Base:
# 	def __init__(self):
# 		self.a = "GeeksforGeeks"
# 		self.__c = "GeeksforGeeks"

# class Derived(Base):
# 	def __init__(self):

# 		Base.__init__(self)
# 		print("Calling private member of base class: ")
# 		print(self.__c)


# # Driver code
# obj1 = Base()
# print(obj1.a)
# # Uncommenting print(obj1.c) will
# # raise an AttributeError

# CLASS

# class Dog:
    
# 	attr1 = "mammal"
# 	attr2 = "dog"
 
# 	def fun(self):
# 		print("I'm a", self.attr1)
# 		print("I'm a", self.attr2)

# Rodger = Dog()

# print(Rodger.attr1)
# print(Rodger.attr2)
# Rodger.fun()

# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
        
#     def show(self):
#         print(f"Hello my name is {self.name} and I work in {self.company}")
        
# obj = GFG("John", "GFG")
# obj.show()

# class Person:
    
#     def __init__(self, name):
#         self.name = name
        
#     def say_hi(self):
#         print(f"Hello !, My name is {self.name}. ")

# obj = Person("Nikhil")
# obj.say_hi()

# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
    
#     def __str__(self):
#         return f"My name is {self.name} and I work in {self.company}"

# obj = GFG("Jonathan", "ST1") 
# print(obj)

# CLASS AND INSTANCE VARIABLES

# class Dog:
#     # class varible
#     animal = "Dog"
    
#     def __init__(self, name,  breed, color):
#         # Instance variable
#         self.name = name
#         self.breed = breed
#         self.color = color
        
#     def show(self):
#         print(f"{self.name} is a {self.animal}")
#         print(f"Breed : {self.breed}")
#         print(f"Color : {self.color} ")
    
# Rodger = Dog("Rodger","Pug", "Brown")
# Buzo = Dog("Buzo","Bulldog", "Black")

# print("Rodger Details : ")
# Rodger.show()

# print("Buzo Details : ")
# Buzo.show()

# class Dog:

# 	# Class Variable
# 	animal = 'dog'

# 	# The init method or constructor
# 	def __init__(self, breed, color):

# 		# Instance Variable
# 		self.breed = breed
# 		self.color = color


# # Objects of Dog class
# Rodger = Dog("Pug", "brown")
# Buzo = Dog("Bulldog", "black")

# print('Rodger details:')
# print('Rodger is a', Rodger.animal)
# print('Breed: ', Rodger.breed)
# print('Color: ', Rodger.color)

# print('\nBuzo details:')
# print('Buzo is a', Buzo.animal)
# print('Breed: ', Buzo.breed)
# print('Color: ', Buzo.color)

# # Class variables can be accessed using class
# # name also
# print("\nAccessing class variable using class name")
# print(Dog.animal)

# class Dog:
#     animal = "Dog"
#     # whatever values we are initializing in __init__ only that values input
#     # is provided when we initialize the object(Rodger) with class(Dog)
#     def __init__(self, breed):
#         self.breed = breed

#     def setcolor(self, color):
#         self.color = color
    
#     def getcolor(self):
#         return self.color
# Rodger = Dog("Pug")
# Rodger.setcolor("Brown")
# print(Rodger.getcolor())

# CONSTRUCTORS 

# class GeeksforGeeks:
#     # default constructor
#     def __init__(self):
#         self.geek = "GeeksForGeeks"
    
#     def print_Geek(self):
#         print(self.geek)
# obj = GeeksforGeeks()
# obj.print_Geek()

# class Addition:
#     first = 0
#     second = 0
#     answer = 0
    
#     # parameterized constructor
#     def __init__(self, f, s):
#         self.first = f
#         self.second = s
        
#     def display(self):
#         print("First Number = ", self.first)
#         print("Second Number = ", self.second)
#         print("Addition of two Numbers : ", self.answer)
        
#     def calculate(self): 
#         self.answer = self.first + self.second
        
# obj1 = Addition(1000, 2000)
# obj2 = Addition(10, 20)
# obj1.calculate()
# obj2.calculate()

# obj1.display()
# obj2.display()
    
# class Myclass:
#     def __init__(self, name = None):
#         if name is None:
#             print("Default Constructor is called")
#         else:
#             self.name = name
#             print("Parameterized Constructor called with name", self.name)
    
#     def method(self):
#         if hasattr(self, 'name'):
#             print("Method called with name", self.name)
#         else:
#             print("Method called without a name")

# obj1 = Myclass()
# obj1.method()
# obj2 = Myclass("John")
# obj2.method()