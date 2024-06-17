class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 100
    
    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is {self.networth}")
        # woh object jiske liye the method is called...if its called for a then shubham, if for b then nitika
a = Person()
b = Person()
c = Person()
a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()
c.info()
    