#Object Oriented Programming
#Functions in OOPs are called methods
#Class--design
#Object--Instance
#Inside Class we have attributes--Variables, Behaviour-- Methods(Function)

class Computer:#Not an inbuilt class , we are creating it
    
    def config(self):
        print("i5, 16gb, 1TB")
        
        
com1=Computer()
com2=Computer()
Computer.config(com1)#To call a function inside class we should mention the class name
Computer.config(com2)

com1.config()
com2.config()