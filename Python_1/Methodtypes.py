#Types of Methods--Instance methods, class methods, static methods
#Types of instance-- Accessor Methods, Mutator Methods
#Accessor--used when we want to only fetch the value
#Mutators--used when we want to modify the value

class Student:
    
    school="ABCD"
    
    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2= m2
        self.m3= m3
    
    def avg(self):
        return(self.m1+ self.m2 + self.m3)/3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self,value):
        self.m1=value
        return value
    
    @classmethod#To create class method we need to use this special symbol
    def getSchool(cls):
        return cls.school 
    
    @staticmethod
    def info():
        print("This is a Student Class....in abc module")        

# s1=Student(56,67,78)
# s2=Student(67,78,89)

# print(s1.set_m1(5))
# print(Student.getSchool())

# print(s1.avg())
# print(s2.avg())

Student.info()


