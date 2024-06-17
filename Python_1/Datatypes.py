#Data Types
# None
# Numeric
# list
# Tuple
# Set
# String
# Range
# Dictionary

# When a variable is not assigned to any value it will return none
# Numeric- int, float, complex, bool
num = 2.5
print(type(num))
num = 2
print(type(num))
num = 2.5+3j
print(type(num))
num = True or False
print(type(num))

a = 5.6
print(type(a))
b = int(a)
print(b)
print(type(b))

c = float(b)
print(c)
print(type(c))

d = 5
e = 6
f = complex(d,e)
print(f)
print(type(f))

print(e < d)

print(int(True))
print(int(False))

#Sequence- List, Tuple, Set, String, Range
A = [12, 23, 34, 45]
print(type(A))

B = {56, 67, 78, 89}
print(type(B))

C = (56, 67, 78, 89)
print(type(C))

D = "Amisha" 
print(type(D))

E = range(10)
print(E)
f = list(E)
print(f)
g = list(range(2,11,2))
print(g)
print(type(range(10)))

#Mapping- Dictionary
#Key should be unique
d = {'rose':'oneplus','mary':'samsung','marlo':'iphone'}
print(d)
print(d.keys())
print(d.values())
print(d['mary'])
print(d.get('marlo'))
