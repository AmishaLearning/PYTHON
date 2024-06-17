def fibonacci(n):
    if n <= 1: 
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter the number : "))

if n <= 1:
    print("Enter a positive number. ")
else:
    print("Fibonacci Series")
    for i in range(n):
        print(fibonacci(i))