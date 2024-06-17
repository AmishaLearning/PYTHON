#Constructor in Inheritance
#Method Resolution Order(MRO)
#Sub class can access all the features of the superclas but the vice versa is not true

# class A:
    
#     def __init__(self):
#         print("in A init")
            
            
#     def feature1(self):
#         print("Feature 1 working")   

#     def feature2(self):
#         print("Feature 2 working")

# class B(A): 
    
#     def __init__(self):
#         super().__init__()#Using this it will call the init function of parent class as well
#         print("in B init")
    
#     def feature3(self):
#         print("Feature 3 working")   

#     def feature4(self):
#         print("Feature 4 working")
        
# # a1=A()
# b1=B()

#Some Other case with Class D having E and F
from typing import Any


class D():
    
    def __init__(self):
        print("in D init")    
            
    def feature1(self):
        print("Feature 1-A working")   

    def feature2(self):
        print("Feature 2 working")

class E(): 
    
    def __init__(self):
        super().__init__()#Using this it will call the init function of parent class as well
        print("in E init")
    
    def feature3(self):
        print("Feature 1-B working")   

    def feature4(self):
        print("Feature 4 working")
        
class F(D,E):
    def __init__(self):
        super().__init__()
        print("in F init")
        
    def feat(self):
        super().feature2()
        
f1=F()
f1.feature1()
f1.feat()  
        