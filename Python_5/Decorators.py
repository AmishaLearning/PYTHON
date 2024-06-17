# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx 

# @greet
# def hello():
#     print("Hello World")

# # @greet
# # def no_hello():
# #     print("No i will not say hello")

# hello()
# # greet(hello) if not giving @greet use this  

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx 

@greet
def add(a, b):
    print(a + b)

add(1, 2)    


