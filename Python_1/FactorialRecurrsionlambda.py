# Factorial Using Recurrsion
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
print(fact(4))


# Anonymous Function or Lambda Function
f = lambda a : a * a
result = f(5)
print(result)

f = lambda a, b : a + b
result = f(5,6)
print(result)