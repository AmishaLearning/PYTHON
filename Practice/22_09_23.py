# Map and Lambda --- fibonacci cube


# def fibonacci(num):
#     a = 0
#     b = 1
#     fibonacci_list = []
    
#     if num <= 0:
#         print("Fibonacci Series not possible")
#     elif num == 1:
#             fibonacci_list.append(a)
#     else:
#         fibonacci_list.append(a)
#         fibonacci_list.append(b)
          
#         for i in range(2, num):
#             c = a + b
#             a = b
#             b = c
#             fibonacci_list.append(c)
#     cube_list = []        
#     for i in fibonacci_list:
#         cube = i ** 3
#         cube_list.append(cube)
#     return cube_list

# num = int(input("Enter the number : "))
# print(fibonacci(num))

cube = lambda x : x ** 3 # Define a lambda function to cube a number

def fibonacci(n):
    a = 0
    b = 1
    fibonacci_list = []
    
    if n <= 0:
        pass
    elif n == 1:
        fibonacci_list.append(a)
    else:
        fibonacci_list.append(a)
        fibonacci_list.append(b)
          
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            fibonacci_list.append(c)
    
    return fibonacci_list

if __name__ == '__main__':
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(list(map(cube, fibonacci(n))))
