#Constructor and Self

class Computer:
    def __init__(self):
        self.name="Rose"
        self.age= 25
        
    # def update(self):
    #     self.age= 30
    
    def compare(self,c2):#Self is c1 here
        if self.age == c2.age:
            return True
        else:
            return False 


c1=Computer()#Constructor
c1.age= 30
c2=Computer()

#Compare(who is calling, whom to compare)
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

# c1.update()#it will upadte c1

print(c1.name)
# print(c1.age)
print(c2.name)
# print(c2.age)