# Array
# Array contains all the values of same type
# No fixed size

# INTEGERS
import array as arr
from array import *#star means everything

vals=array('i',[5,6,7,8,9])
print(vals)

vals=array('i',[5,6.5,7,8,9])
print(vals)#error as float value is present
#'I' means only positive numbers

print(vals.buffer_info())#(address,size)

print(vals.typecode)
# vals.reverse()

print(vals[2])

for i in range(5):
    print(vals[i])
    
for i in range(len(vals)):
    print(vals[i])

for i in vals:
    print(i)


vals1=array('u',['a','e','i','o'])

for i in vals1:
    print(i)

newArr=array(vals.typecode,[a**2 for a in vals])
for i in newArr:
    print(i)
    
i=0
while i<len(newArr):
    print(newArr[i]) 
    i+=1 

#Array input from user

from array import *
arr=array('i',[])
n=int(input("Enter the length of the array :"))

for i in range(n):
    x=int(input("Enter the next Value :"))
    arr.append(x)
print(arr)

val=int(input('Enter the value to search :'))
k=0
for e in arr:
    if e==val:
        print(k)
    k+=1
    
print(arr.index(val))