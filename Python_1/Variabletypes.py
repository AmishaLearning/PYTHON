#Variables--Instance variable and class(static) variable

class Car:#Variables outside init but within the class are called Class Variables
    
    wheels= 4#Class namespace
        
    def __init__(self):#variable inside init in called instance variable
        self.mil= 10#
        self.com="BMW"#Instance namespace
        
        
c1=Car()
c2=Car()

c1.mil= 8
Car.wheels=5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)

