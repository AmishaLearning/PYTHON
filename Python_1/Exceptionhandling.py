#Exception Handlingp
#Types of errors
#Compile : missing colon, spelling mistake
#Logical : getting wrong output
#Runtime : divide by 0

a=5
b=0


try:
    print("resource open")
    print(a/b)#after getting the error it is jumping out of the block 
    k=int(input("Enter a number :"))
    print(k)
    
except ZeroDivisionError as e:
    print("Hey!!, you can't divide a number by zero",e)
    
except ValueError as e:
    print("Invalid Input")
    
except Exception as e:
    print("Something went wrong")
    
finally:#it doesn't matter that u are getting exception or not this will execute
    print("resource closed")