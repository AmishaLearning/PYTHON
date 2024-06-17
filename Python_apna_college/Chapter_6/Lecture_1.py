print("--------------------------------Functions--------------------------------")

# # funcation definition
# def summation(a, b): # parameters
#     sum = a + b 
#     return sum

# print(summation(5, 7)) # function call; 5, 7 : arguments

# def func_average(a, b, c):
#     average = (a + b + c) / 3 
#     return average

# print(func_average(2, 4, 6))
    
# print("-------------------------Deafult Parameters--------------------------------")

# def cal_prod(a= 3, b = 2):
#     print(a * b)
#     return a * b

# cal_prod()

# print("-------------------------Recurrsion--------------------------------")

# def show(n):
#     if(n == 0):
#         return # returning control
#     print(n)
#     show(n - 1)
# show(5)

# def show(n):
#     if(n == 0):
#         return # returning control
#     print(n)
#     show(n - 1)
#     print("END")
# show(5)

print("------------------------Recursion Factorial-----------------------------")

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)
    
num = int(input("Enter the number to find it's Factorial: "))
print("The Factorial of", num, "is :" ,fact(num))