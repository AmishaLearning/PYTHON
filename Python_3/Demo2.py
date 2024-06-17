# class Myclass:
#     pass
# x=5
# print(type(x))
# print(isinstance(x,1))

# temp = 10   # global-scope variable
# def func():
#      temp = 20   # local-scope variable
#      print(temp)
# print(temp)  
# func()    
# print(temp)

temp = 10   # global-scope variable
def func():
    global temp  # local-scope variable
    temp = 20
    print(temp)
print(temp)  
func()    
print(temp)  
