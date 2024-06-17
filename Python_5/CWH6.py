# def average(a, b):
#     print("The average is ", (a+b)/2)
# average(4, 6)
# #Four types of arguments
# # Default, Keyword, Variable length, Required
# # In the above case 
# #a, b are required arguments

# def average(a=8, b=2):
#     print("The average is ", (a+b)/2)
# average()

# #a, b became default arguments

# def average(a=8, b=2):
#     print("The average is ", (a+b)/2)
# average(1, 9)
# #this will ignore the default value 8 and 2 and will consider 1 and 9
# # we can also provide one value like a= 5 then be will have default value as 2

# def average(a=8, b=2):
#     print("The average is ", (a+b)/2)
# average(b=1, a=5)
# # Order doesn't matter if we specify the element


# #REQUIRED ARGUMENTS
# # in the above example it is necessary to give the value of a and b so those are required arguments

# #VARIABLE LENGTH ARGUMENTS
# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("The Average is : ", sum/(len(numbers)))
    
# average(4, 3, 3)

# def name(**name):
#     # print(type(name))
#     print("Hello !,", name["fname"], name["mname"], name["lname"])

# name(mname = "Paglu", lname = "Taklu", fname = "Something")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/(len(numbers))
    
c = average(4, 3, 3)
print(c)

# if more than one return statement is there in a function...The first one will be considered rest all will be ignored

