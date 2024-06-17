#Special Variable __name__
# if we are importing nameusedinspecialvariablename in another module it will print the name of the module 
# import Calspecialvariablename

# print("Demo Says "+ __name__)

# def main():
#     print("Hello!!")
#     print("Welcome User")


# if __name__=="__main__":
#     main()
from Calspecialvariablename import add

def fun1():
    add()
    print("From Fun1")
    
def fun2():   
    print("From Fun2")
    
def main():
    fun1()
    fun2()
main()