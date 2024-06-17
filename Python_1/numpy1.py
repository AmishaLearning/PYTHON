from numpy import *

arr=array([1,2,3,4],int)
print(arr)

#ways to create array in numpy 
#array(), linespace(), logspace(), arange(), zeros(), ones()

#creating array with array()
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)
arr=array([1,2,3,4,5.0])
print(arr)
print(arr.dtype)
# all values will be converted to float

arr=array([1,2,3,4,5],float)#all values are int but mentioned float it will conver the value to floats
print(arr)


#Create array with linspace()
arr1=linspace(0,15,16)#(start,stop,parts)by default parts= 50
print(arr1)
arr1=linspace(0,15)
print(arr1)

#Create array with arange()
arr2= arange(1,15,2)# print numbers skipping 2 numbers
print(arr2)

#Create array with logspace()
arr3=logspace(1,40,5)#spacing depends on log of number
print(arr3)
print('%.2f' %arr3[0])#fpr printing 2 digits after decimal

#Create array with zeros()
arr4=zeros(5)
print(arr4)#printitng array of Zeros

#Create array with ones()
arr5=ones(5)
print(arr5)#priting array of ones
