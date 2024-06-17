#Scope
a = 10#Global variable

def something():
    a = 15#local variable
    
    print("In function",a)

something()    
print("outside",a)

#If we don't have local variable
#A global variable can be assessed inside a function as well
a = 10#Global variable

def something():  
    print("In function",a)

something()    
print("outside",a)

#Explicitly specify the global variable inside function to change the global variables value

a = 10#Global variable
def something():
    global a
    a = 15#local variable
    print("In function",a)

something()    
print("outside",a)
#there can't be a local and a global variable of same name in a function