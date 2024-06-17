# ENCAPSULATION

# class Base:
#     def __init__(self):
#         self._a = 2

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling Protected member of base class : ", self._a)

#         self._a = 3
#         print("Calling Modified protected member outside class : ", self._a)

# obj1 = Derived()
# obj2 = Base()

# print("Accessing protected member of obj1 : ", obj1._a)
# print("Accessing protected member of obj2 : ", obj2._a)

# POLYMORPHISM

# class India:
#     def capital(self):
#         print("New Delhi is the Capital of India")
#     def language(self):
#         print("Hindi is the most widely spoken language in India")
#     def type(self):
#         print("India is a developing country")

# class USA:
#     def capital(self):
#         print("Washington, D.C. is the capital of USA")
#     def language(self):
#         print("English is the primary Language of USA")
#     def type(self):
#         print("USA is a Developed Country")

# obj_ind = India()
# obj_usa = USA()

# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()
        
# class CSStudent:
#     stream = "CSE"
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

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
# # b.stream = "CIVIL"
# print(b.stream)

# CSStudent.stream = "MECH"
# print(a.stream)
# print(b.stream)

# CLASS AND STATIC METHODS

# STATIC METHOD 

# class Calculator:
#     def __init__(self, version):
#         self.version = version
        
#     def description(self):
#         print(f"Currently Calculator is running on Version : {self.version}")
    
#     @staticmethod
#     def add_number(*numbers : float) -> float:
#         return sum(numbers)
    
# calc1 = Calculator(10)
# calc2 = Calculator(100)

# calc1.description()
# calc2.description()

# print(Calculator.add_number(10, 20, 30))

# METHOD RESOLUTION ORDER

# class A:
#     def rk(self):
#         print("Class A")

# class B(A):
#     def rk(self):
#         print("Class B")
    
# result = B()
# result.rk()

# # EXAMPLE 1
# class A:
# 	def rk(self):
# 		print(" In class A")
# class B(A):
# 	def rk(self):
# 		print(" In class B")
# class C(A):
# 	def rk(self):
# 		print("In class C")

# # classes ordering
# class D(B, C):
# 	pass
	
# r = D()
# r.rk()

# EXAMPLE 2
# class A:
#     def rk(self):
#         print("In Class A")

# class B:
#     def rk(self):
#         print("In Class B")

# class C(A):
#     def rk(self):
#         print("In Class C")

# class D(B):
#     def rk(self):
#         print("In Class D")

# class E(C, D):
#     # def rk(self):
#     #     print(E.mro())
#     pass
        
# result = E()
# result.rk()
