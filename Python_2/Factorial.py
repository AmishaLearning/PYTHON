# def trial():
#     a= "Hello!"
#     return a

# result= trial()
# print(result)

# num=int(input("Enter the number to find it's Factorial: "))
# f=1
# if num<0:
#     print("The factorial is not possible for Negative Numbers")
    
# elif num == 0:
#     print("Factorial of 0 is 1")
        
# else:
#     if num>0:
#         for i in range(1,num+1):
#             f=f*i
#         print("The Factorial of ",num, "is", f)
    
# #if return statement is not given output will come as NONE 
# #In function to get output it is necessary to give return

# def factorial(n):
#     if (n == 0 or n ==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# num=int(input("Enter the number to find it's Factorial: "))
# print("The Factorial of ",num,"is :" ,factorial(num))

#Ternary Operator

def factorial(n):
    return 1 if (n == 0 or n == 1) else n*factorial(n-1)

num=int(input("Enter the number to find it's Factorial: "))
print("The Factorial of ",num,"is :" ,factorial(num))


    
