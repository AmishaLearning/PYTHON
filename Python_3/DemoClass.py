# class InterviewBit:
#     def __init__(self,emp_name):
#         self.employeename=emp_name
    
#     def intro(self):
#         print("Hello! I am ", self.employeename)

# emp_1=InterviewBit("Mr. Employee")
# print(emp_1.employeename)
# emp_1.intro()

class Parent(object):
    pass
class child(Parent):
    pass

#The method tells us if any class is a child of another class by returning true or false accordingly
print(issubclass(child,Parent))
print(issubclass(Parent,child))

#We can check if an object is an instance of a class by making use of isinstance() method

obj1=Parent()
obj2=child()
print(isinstance(obj1,child))
print(isinstance(obj2,child))