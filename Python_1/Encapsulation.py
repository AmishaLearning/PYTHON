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
# # print(obj1.__c)
# #__c is a private attribute thats why it can't be called from outside



# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
 
#     def __str__(self):
#         return f"My name is {self.name} and I work in {self.company}."
 
 
# my_obj = GFG("John", "GeeksForGeeks")
# print(my_obj)

# class Addition:
#     first = 0
#     second = 0
#     answer = 0
 
#     # parameterized constructor
#     def __init__(self, f, s):
#         self.first = f
#         self.second = s
 
#     def display(self):
#         print("First number = " + str(self.first))
#         print("Second number = " + str(self.second))
#         print("Addition of two numbers = " + str(self.answer))
 
#     def calculate(self):
#         self.answer = self.first + self.second
 
 
# # creating object of the class
# # this will invoke parameterized constructor
# obj1 = Addition(1000, 2000)
 
# # creating second object of same class
# obj2 = Addition(10, 20)
 
# # perform Addition on obj1
# obj1.calculate()
 
# # perform Addition on obj2
# obj2.calculate()
 
# # display result of obj1
# obj1.display()
 
# # display result of obj2
# obj2.display()


# Python program to
# demonstrate protected members
  
# Creating a base class
class Base:
    def __init__(self):
  
        # Protected member
        self._a = 2
  
# Creating a derived class
class Derived(Base):
    def __init__(self):
  
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ", 
              self._a)
  
        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)
  
  
obj1 = Derived()
  
obj2 = Base()
  
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)
  
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)