#we have created a class named Dog using the class keyword
# class dog:
#     pass
# obj=dog()

#Creating a class and object with class and instance attributes

# class dog:
    
#      #class attribute
#      attr1 = "Mammal"
     
#      #Instance attribute
#      def __init__(self,name):
#          self.name = name
         
# #Driver Code
# #Object Instantiation
# Rodger = dog("Rodger")
# Tommy = dog("Tommy")

# #Accessing class attributes
# print("Rodger is a {} ".format(Rodger.__class__.attr1))
# print("Tommy is a {} ".format(Tommy.__class__.attr1))

# #Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))


# class Dog:
 
#     # class attribute
#     attr1 = "mammal"
 
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
         
#     def speak(self):
#         print("My name is {}".format(self.name))
 
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
 
# # Accessing class methods/functions 
# Rodger.speak()
# Tommy.speak()



# Python code to demonstrate how parent constructors are called.

#Parent class
class Person(object):
    
    #__init__ is known as constructor
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("My name is {} ".format(self.name))
        print("IdNumber : {} ".format(self.idnumber))

#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        
    def details(self):
        print("My name is {} ".format(self.name))
        print("Idnumber :{} ".format(self.idnumber))
        print("Post : {} ".format(self.post))
        
# creation of an object variable or an instance
a = Employee('Max', 987654, 20000, 'Test')

# calling a function of the class Person using its instance
a.display()
a.details()


# #Polymorphism
# class Bird:
    
#     def intro(self):
#         print("There are many types of birds.")
        
#     def flight(self):
#         print("Most of the birds can fly but some cannot")
    
# class Sparrow(Bird):
    
#     def flight(self):
#         print("Sparrows can fly")
        
# class Ostrich(Bird):
    
#     def flight(self):
#         print("Ostrich cannot fly")
        
# obj_bird = Bird()
# obj_spr = Sparrow()
# obj_ost = Ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()

#Encapsulation


# Python program to demonstrate private members
 
# # Creating a Base class
# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks"
 
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
 
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
 
 
# # Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1.c)