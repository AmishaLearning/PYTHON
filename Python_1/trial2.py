# # Initialize an empty dictionary
# D = {}
 
# L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]
 
# # Loop to add key-value pair
# # to dictionary
# for i in range(len(L)):
#     # If the key is already
#     # present in dictionary
#     # then append the value
#     # to the list of values
#     if L[i][0] in D:
#         D[L[i][0]].append(L[i][1])
     
#     # If the key is not present
#     # in the dictionary then add
#     # the key-value pair
#     else:
#         D[L[i][0]]= []
#         D[L[i][0]].append(L[i][1])
#     print(D)


# roll_no = [10, 20, 30, 40, 50]
# names = ['Ramesh', 'Mahesh', 'Kamlesh',
#          'Suresh', 'Dinesh']
 
# students = dict(zip(roll_no, names))
# print(students)

# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "green"]
# for fruit, color in zip(fruits, colors):
#     print(fruit, "is", color)

# # Single statement while block
# count = 0
# while (count < 5): count += 1; print("Hello Geek")

# generator_exp = (i * 5 for i in range(5) if i%2==0)
 
# for i in generator_exp:
#     print(i)


# A simple generator for Fibonacci Numbers
# def fib(limit):
     
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
 
#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b
 
# # Create a generator object
# x = fib(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# sqr = lambda a : a ** 2
# num = 5
# print(f"Square of {num} is {sqr(num)}")

# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Function to be decorated
@my_decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()