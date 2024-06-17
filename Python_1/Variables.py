num=5
print(id(num))
name="Amisha"
print(id(name))
a=10
b=a
print(a,b)
#Whenever we create multiple variables with same data they will point to one box only
print(id(a))
print(id(b))
print(id(10))
# In python we can't make constants
print(type(a))
print(type(name))
