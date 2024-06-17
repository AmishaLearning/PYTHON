# inheritence
# Single Level Inheritence
# class A:#Parent or Super Class
#     def feature1(self):
#         print("Feature 1 working")   

#     def feature2(self):
#         print("Feature 2 working")

# class B(A):#B is the child class or Sub Class of A (class B is inheritring all the features from A)      
    
#     def feature3(self):
#         print("Feature 3 working")   

#     def feature4(self):
#         print("Feature 4 working") 
        
# class C(B):
#     def feature5(self):
#         print("Feature 5 working") 
    
        
# a1 = A()
# a1.feature1()
# a1.feature2()
# print("------------")
# b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()
# print("------------")
# c1 = C()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()

#Multilevel or multiple inheritence
class D:#Parent or Super Class
    def feature1(self):
        print("Feature 1 working")   

    def feature2(self):
        print("Feature 2 working")

class E():
    
    def feature3(self):
        print("Feature 3 working")   

    def feature4(self):
        print("Feature 4 working") 
        
class F(D,E):
    def feature5(self):
        print("Feature 5 working") 
        
f1=F()
f1.feature1()
f1.feature2()
f1.feature3()
f1.feature4()
f1.feature5()
    
    
# Python code to demonstrate how parent constructors
# are called.

# class Person(object):#Class A
 
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
 
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#         print("This id from class A")
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("This is from class A")
     
# # child class
# class Employee(Person):#Class B
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
 
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))
#         print("This is from class B")
 
# # creation of an object variable or an instance
# b = Employee('Rahul', 886012, 200000, "Intern")
 
# # calling a function of the class Person using
# # its instance
# b.display()
# b.details()

# a = Person("Amisha", 12345)
# print("-------------------------------")
# a.details()
# a.display()


# class C(object):
#     def __init__(self):
#         self.c = 21
 
#         # d is private instance variable
#         self.__d = 42
        
# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)
 
# object1 = D()
 
# # produces an error as d is private instance variable
# print(object1.c)
# print(object1.__d)

