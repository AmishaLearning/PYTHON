# FOR AND ELSE

# for i in range(5):
#     print(i)
    
# else:
#     print("Out of Index")

# i = 0
# while i < 4:
#     print("Yess!! I am less than 4")
#     i = i + 1 
# else:
#     print("Oh No!! I am greater than 4")        

# for i in range(6):
#     print(i)
#     if i == 4:
#         break
    
# else:
#     print("Sorry!! No i")
    
#if else is being executed this means....loop has ended not broken

#TRY EXCEPT

# a = input("Enter the number : ")
# print(f"The multiplication Table of {a} is : ")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
        
# except Exception as e:
#     print("The error is : ",e)
    
    
# print("Some important lines of Code")
# print("End of Program")


#TRY EXCEPT FINALLY
#Finally block is always executed irrespective of try and except is running or not

# try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index : "))
#     print(l[i])
    
# except:
#    print("Some error occured.") 
   
# finally:
#     print("I am always executed")

# def func1():
#     try:
#         l = [1, 5, 6, 7]
#         i = int(input("Enter the index : "))
#         print(l[i])
#         return 1
    
#     except:
#         print("Some error occured.") 
#         return 0
#     finally:
#         print("I am always executed")

# x = func1()
# print(x)


# def func1():
#     try:
#         l = [1, 5, 6, 7]
#         i = int(input("Enter the index : "))
#         print(l[i])
#         return 1
    
#     except:
#         print("Some error occured.") 
#         return 0
#     print("I am always executed")#this statement will not be executed
# x = func1()
# print(x)


#CUSTOM ERRORS

a = input("Enter a value between 5 and 9 :")

if "quit" in a:
        pass
elif int(a) < 5 or int(a) > 9:
    raise ValueError("Value should be between 5 and 9") 
else:
    print("Good!! You entered a value between 5 and 9")