#APPROACH 1 
# list1=[1,2,3,4,5,6,7,8,9]
# Mul=1

# for i in range(0,len(list1)):
#     Mul=Mul*list1[i]
    
# print("The Multiplication of the elements is : ",Mul)

#APPROACH 2 USING numpy package
import numpy

list2=[3,2,4,1,4,5,3,7]
Multi=numpy.prod(list2)
print("The Multiplication of the elements is : ",Multi)