# def double(x):
#     return x * 2

double = lambda x : x * 2

print(double(5))

cube = lambda x : x ** 3
print(cube(8))

avg = lambda x, y : (x + y)/2
print(avg(5, 5))

avg2 = lambda x, y, z : (x ** y) + z
print(avg2(1, 4, 5)) 

def appl(fx, value):
    return 6 + fx(value)
print(appl(cube, 2))

def check(func, num):
    return 6 + func(num)

print(check(lambda x : x ** 2, 3))