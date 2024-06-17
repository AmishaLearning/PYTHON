#Decorators
#everytime i want the numerator to be greater than denominator in division
# def div(a,b):
#     if a<b:
#         a,b=b,a
#     print(a/b)
# div(2,4)

#Swapping the values without changing the function

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div=smart_div(div)

div(2,4)