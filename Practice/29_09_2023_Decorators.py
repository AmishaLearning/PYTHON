# TREATING FUNCTIONS AS OBJECTS

# def shout(text):
#     return text.upper()

# print(shout("hello"))

# yell = shout
# print(yell("HeLlO"))

# Passing the function as an argument 

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(func):
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print(greeting)
    
# greet(shout)
# greet(whisper)

# Returning functions from another function.

# def create_adder(x):
#     print("I am from create_adder")
#     def adder(y):
#         print("I am from adder")
#         return x + y
#     return adder

# add_15 = create_adder(15)
# print(add_15(10))

# Decorator can modify the behaviour

# def hello_decorator(func):
#     def inner1():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner1

# def function_to_be_used():
#     print("This is inside the function !!")

# function_to_be_used = hello_decorator(function_to_be_used)
# function_to_be_used()
           
# TRIAL
                
# def start(end):
#     print("I am from start")
#     def inner1():
#         print("I am from inner!")
#         end()
#     return inner1

# @start
# def end():
#     print("I am from end")
    
# end()

# What if a function returns something or an argument is passed to the function?

# def hello_decorator(func):
#     def inner1(*args, **kwargs):
#         print("Before Execution")
        
#         returned_value = func(*args, **kwargs)
#         print("After Execution")
        
#         return returned_value
#     return inner1

# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b

# a, b = 1, 2
# print("Sum = ", sum_two_numbers(a, b))

# CHAINING DECORATORS

# def decor1(func):
#     print("I am decor1")
#     def inner():
#         x = func()
#         print(x)
#         return x * x
#     return inner

# def decor(func):
#     print("I am decor")
#     def inner():
#         x = func()
#         return 2 * x
#     return inner

# @decor1
# @decor
# def num():
#     return 10

# @decor
# @decor1
# def num1():
#     return 10

# print(num())
# print(num1())

# METHOD RESOLUTION ORDER (MRO)

# class A:
#     def rk(self):
#         print("I am in class A")
        
# class B(A):
#     def rk(self):
#         print("I am from class B")
        
# r = B()
# r.rk()

# class A:
#     def rk(self):
#         print("In class A")
# class B(A):
#     def rk(self):
#         print("In class B")
# class C(A):
#     def rk(self):
#         print("In class C")
    
# class D(B, C):
#     print("In class D")

# r = D()
# r.rk()

# class A:
#     def rk(self):
#         print("In class A")
# class B:
#     def rk(self):
#         print("In class B")
# class C(A, B):
#     def __init__(self):
#         print("Constructor C")

# r = C()
# print(C.__mro__)

