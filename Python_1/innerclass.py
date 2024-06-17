class Student:#Outer Class
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
        
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
        
        
    class laptop:#Inner Class
        def __init__(self):
            self.brand ="HP"
            self.cpu   ="i5"
            self.ram   = 8   
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
                 
    
    
s1=Student('Rose',12)
s2=Student('Mary',23)

# print(s1.name,s1.rollno)

s1.show()
# lap1= s1.lap.brand
# lap2= s2.lap.cpu
# print(lap1)
# print(lap2)

# print(id(lap1))
# print(id(lap2))


