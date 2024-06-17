# del Keyword 

# class Student:
#     def __init__(self, name):
#         self.name = name
        
# s1 = Student("Amisha")
# print(s1.name)
# del s1.name
# print(s1.name)

# print("------------------------Private/Public Attributes----------------")

# Private and Public attributes

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
    
#     # we are able to access the private attribute here because this function is inside the class
#     def reset_pass(self):
#         print(self.__acc_pass)
        
# acc1 = Account(654321, "password")
# acc1.reset_pass()
# print(acc1.acc_no, acc1.__acc_pass)

# class Person:
#     __name = "Anonymous"
    
#     def __hello(self): # Private function
#         print("Hello Person")
        
#     def welcome(self):
#         self.__hello()
        
# p1 = Person()
# # print(p1.__name)
# p1.welcome()

print("-----------------------------------Inheritance--------------------------------")

# # SINGLE INHERITANCE

# class Car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car Started")
    
#     @staticmethod
#     def stop():
#         print("Car Stopped")
        
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")    

# print(car1.name)
# print(car2.name)  
# car1.start()
# print(car1.color)
        
# # MULTIPLE INHERITANCE

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started")
#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand 
        
# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()
        
# # MULTIPLE INHERITANCE

# class A:
#     varA = "Welcome to class A"
# class B:
#     varB = "Welcome to class B"
# class C(A, B):
#     varC = "Welcome to class C"
    
# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
    
# # super() method

# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car Started")
#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()    
        

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# # Class Method

# class Person:
#     name = "Anonymous"
    
#     def changeName(self, name):
#         self.name = name
    
# p1 = Person()
# p1.changeName("Random")
# print(p1.name)
# print(Person.name)

# class Person_1:
#     name = "Anonymous_1"
    
#     def changeName(self, name):
#         Person_1.name = name
    
# p1 = Person_1()
# p1.changeName("Random_1")
# print(p1.name)
# print(Person_1.name)

# class Person_2:
#     name = "Anonymous_2"
    
#     def changeName(self, name):
#         self.__class__.name = "Random_3"
        
# p1 = Person_2()
# p1.changeName("random_small")
# print(p1.name)
# print(Person_2.name)

# class Person:
#     name = "Anonymous"
    
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
        
# p1 = Person()
# p1.changeName("Ram")
# print(p1.name)
# print(Person.name)

# # PROPERTY DECORATOR

# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#         self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"
        
#     def calculatepercentage(self):
#         self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

        
# stu1 = Student(98, 97, 99)
# print(stu1.percentage)
        
# stu1.phy = 86
# print(stu1.phy)
# print(stu1.percentage) # this will not change automatically

# stu1.calculatepercentage() # this will change automatically
# print(stu1.percentage) 

# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.maths)/3) + "%"

        
# stu1 = Student(98, 97, 99)
# print(stu1.percentage)
        
# stu1.phy = 86
# print(stu1.percentage) 

# # POLYMORPHISM

# print(1 + 2) # 3
# print("apna" + "college") # concatenation
# print([1, 2, 3] + [4, 5, 6]) # merge

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real, "i +", self.img, "j")
        
    # def add(self, num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal, newImg)
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
        

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

    
