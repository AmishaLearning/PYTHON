#Filter(),map(),reduce()

#FILTER
def is_even(n):
    return n%2==0
  
nums=[3,2,6,8,4,6,2,9]
evens=list(filter(is_even,nums))
# print(evens)

# even=list(filter(lambda n: n%2==0,nums))
# print(even)

# #MAP
# def update(n):
#     return n+2

doubles=list(map(lambda n: n*2,evens))
#REDUCE
#need to import reduce from functools
from functools import reduce

def add_all(a,b):
    return a+b

# sum= reduce(add_all,doubles)

sum=reduce(lambda a,b:a+b, doubles)
print(doubles)
print(sum)


