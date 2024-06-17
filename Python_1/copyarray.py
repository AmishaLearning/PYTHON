from numpy import *

arr=array([1,2,3,4,5])

arr=arr+5
print(arr)

arr1=array([2,4,6,8])
arr2=array([1,3,5,7])
print(arr1+arr2)

print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))

arr3=array([67,34,12,99,342,89])
print(sort(arr3))

#concatenate 2 arrays
print(concatenate([arr1,arr2]))

# copy two array

arr4=array([1,3,6,9])
arr5=arr4
print(arr4)
print(arr5)
print(id(arr4))
print(id(arr5))

arr5=arr4.view()#view(a function which helps to create a new array in a new location)
print(arr4)
print(arr5)
print(id(arr4))#Different address
print(id(arr5))

# Types of copy--shallow copy and Deep copy
# shallow copy means it will copy the elements but still both arrays are dependent on each other
arr4[1]=89
print(arr4)
print(arr5)#value changes for both arr4 and arr5
print(id(arr4))
print(id(arr5))

# deep copy--two arrays are not linked to each other in any way

arr5=arr4.copy()
arr4[1]=90

print(arr4)# it will have new value
print(arr5)# it contains the old vale
print(id(arr4))
print(id(arr5))

# Assignment Question
arr1=array([1,2,3,4])
arr2=array([1,2,3,4])
x=[]
for i in range(4):
    i= arr1[i]+arr2[i]
    x.append(i)
print(x)

arr1=array([45,3,6,12,35])

arr2=sort(arr1)
print(arr2)

print("the minimum value is :",arr2[0])