# # matrixx
from numpy import*

# arr1=array([
#             [1,2,3,4,5,6],
#             [4,5,6,7,8,9]
# ])

# print(arr1)
# print(arr1.dtype)
# print(arr1.ndim)#Gives the dimension of the array
# print(arr1.shape)#Gives number of rows and columns
# print(arr1.size)#gives size of the entire block

# #Converting 2d to 1d array
# arr2=arr1.flatten()
# print(arr2)

# #converting 1d to 2d
# arr3=arr2.reshape(3,4)
# print(arr3)

# #Converting to 3d array
# arr3=arr2.reshape(2,2,3)
# print(arr3)


# arr4=array([
#             [1,2,3,4],
#             [4,5,6,7]
# ])

# # m=matrix(arr4)
# # print(m)

# #string to matrices
# m1=matrix('1 2 3 ; 6 4 5  ; 1 6 7 ')#Semicolon to separate each row
# print(m1)

# #Print diagonal elements only
# print(diagonal(m1))
# print(m1.min())
# print(m1.max())

m2=matrix('1 2 3 ; 6 4 5  ; 1 6 7 ')
m3=matrix('1 2 3 ; 6 8 5  ; 2 6 7 ')

m4=m2+m3
print(m4)

m5=m2*m3
print(m5)
