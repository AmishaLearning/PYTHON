# Function Arguments

def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x ",x)
 
a=10    
# update(10)
update(a)
print("a ",a)

# Pass by value-- means passing a value not an address
# Pass by reference-- means passing a address

def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print("x ",lst)
    
lst=[10,20,30]
print(id(lst))
update(lst)
print("lst ",lst)

# TYPES OF ARGUMENTS

def sum(a,b):#Formal Arguments
    c=a+b
    print(c)
    
sum(6,9)#Actual Arguments
# Actual Arguments have 4 types--Position, Keyword, Default, Variable Length

def person(name,age):
    print(name)
    print(age)
    
person('rose',26)
# Position matters here in order to check the correct position where the variable is assigned to its value ...we can't exchange the values

# KEYWORDS
# Suppose function is defined somewhere else n we are not sure about the position of the variables in that case we use keywords

def person(name,age):
    print(name)
    print(age)
    
person(age=26,name='Rose')

# DEFAULT
def person(name,age=18):#Default value of age in function
    print(name)
    print(age)
    
person('Rose',20)#if we provide age here it will over write the value in the function

# VARIABLE LENGTH
# *b means it can have multiple values
def sum_1(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
   
sum_1(21,12,1,2,4,3)
    
def sum_2(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
   
sum_2(21,12,1,2,4,3)

