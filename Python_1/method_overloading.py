#Method Overloading Method Overriding
#Method Overloading:In a class if we have two methods with same name but different parameters.
#Method Overriding: In two diffrernt classes if we have two methods with same name and same parameters.

#METHOD OVERLOADING
# class Student:
    
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2

# #If we want to pass only 2 values and in result no error should appear for that we should pass None for all values in the method    
#     def sum(self,a=None,b=None,c=None):
#         s=0
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None:
#             s=a+b
#         else:
#             s=a
#         return s
    
# s1=Student(58,69)

# print(s1.sum(5,9))

#METHOD OVERRIDING 

class A:
    
    def show(self):
        print("in A Show")
        
class B(A):
    def show(self):
        print("in B Show")
        
a1= B()
a1.show()