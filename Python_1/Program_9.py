#Python Operators
a = 5
b = 6

if a == b:
    print("a == b")
if a != b:
    print("a != b")
if a > b:
    print("a > b")
if a < b:
    print("a < b")
if a >= b:
    print("a >= b")
if a <= b:
    print("a <= b")
else:
    print("No!")
    
c = 8
d = 7
 
if c > d and c >= d:
    print("Yes!")
else:
    print("No!")

e = 9
f = 10
    
if e > f or e == f:
    print("Yes")
else:
    print("No!")
    
if not(e != f):
    print("Yes")
else:
    print("No!")
    
x = 12
y = 21

if x is y:
    print("True")
else:
    print("False")
    
if x is not y:
    print("False")
else:
    print("True")
    
v=["apple","mango","banana","kiwi"]

print("grapes"in v)
print("grapes" not in v)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(8 >> 2)
print(8 << 2)