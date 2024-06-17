#init function (Special Method)
#init will be called automatically
#in output we are getting in init 2 times because we are calling 2 objects
class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu= cpu
        self.ram= ram        
        
    def config(self):
        print("Config is :",self.cpu,self.ram)
        
com1=Computer('i5',16)#This will call init
com2=Computer('Ryzen 3',8)

com1.config()
com2.config()