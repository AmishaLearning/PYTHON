#Output Variables
x="Python is Awesome"
print(x)

a="Python "
b="is "
c="Awesome "
print(a,b,c)
print(a + b+ c)

d=3
e=5
print(d+e)
print(a+str(e))

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) 
# are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

y= "Awesome"
def myfunc():
    print("Python is " + y)
myfunc()

g="Awesome"

def myfunc1():
    g="Fantastic"
    print("Python is " +g)

myfunc1()
print("Python is " + g) 
   
#Global Variable
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc2():
    global j
    j="fantastic"
myfunc2()

print("Python is " +j)
    