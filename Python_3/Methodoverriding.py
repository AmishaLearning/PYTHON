class A:
    def func1(self):
        print("Feature 1 from Class A")
        
    def func2(self):
        print("Feature 2 from Class A")
        
class B(A):
    #Modifying function that is already present in Class A
    
    def func1(self):
        print("Feature 1 from Class B")
    
    def func3(self):
        print("Feature 3 from class B")
        
obj = B()
obj.func1()
obj.func2()
obj.func3()