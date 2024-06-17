# Array
# import numpy

# a = numpy.array([1, 2, 3, 4, 5])
# print(a[1])

# b = numpy.array([1, 2, 3, 4, 5], float)
# print(b[1])


# nums = list(map(int, input("Enter the numbers : ").split()))
# nums_array = numpy.array(nums, float)
# reversed_array = nums_array[::-1]

# print(reversed_array)

# Array Mathematics

# a = numpy.array([1, 2, 3, 4], float)
# b = numpy.array([5, 6, 7, 8], float)

# print(a + b)
# print(numpy.add(a, b))

# print(a - b)
# print(numpy.subtract(a, b))

# print(a * b)
# print(numpy.multiply(a, b))

# print(a / b)
# print(numpy.divide(a, b))

# print(a % b)
# print(numpy.mod(a, b))

# print(a ** b)
# print(numpy.power(a, b))

# import numpy

# dimension = list(map(int, input("Enter the value of N X M : ").split()))
# values_A = []
# values_B = []

# for i in range(dimension[0]):
#     values_A.extend(list(map(int, input("Enter the values in A : ").split())))
    
# for j in range(dimension[0]):
#     values_B.extend(list(map(int, input("Enter the values in B : ").split())))

# A = numpy.array(values_A).reshape(dimension[0], dimension[1])
# B = numpy.array(values_B).reshape(dimension[0], dimension[1])

# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)
# print(A ** B)

# Floor, Ceil, Rint

# import numpy

# #my_array = numpy.array(list(map(float, input("Enter the Values: ").split())))

# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# numpy.set_printoptions(legacy = '1.13')
# print(numpy.floor(my_array))

# print(numpy.ceil(my_array))

# print(numpy.rint(my_array))

# Sum and Prod

# import numpy 

# my_array = numpy.array([[1, 2], [3, 4]])
# print("ADDITION")

# print(numpy.sum(my_array, axis = 0))
# print(numpy.sum(my_array, axis = 1))
# print(numpy.sum(my_array, axis = None))
# print(numpy.sum(my_array))

# print("MULTIPLICATION")
# print(numpy.prod(my_array, axis = 0))
# print(numpy.prod(my_array, axis = 1))
# print(numpy.prod(my_array, axis = None))
# print(numpy.prod(my_array))

# import numpy

# values = list(map(int, input().split()))

# values_A  = numpy.array(list(map(int, input().split())))
# values_B  = numpy.array(list(map(int, input().split())))

# result1 = numpy.array([[values_A], [values_B]])
# result2 = numpy.sum(result1, axis = 0)
# print(numpy.prod(result2))


# import numpy as np

# N, M = map(int, input("Enter the value of N and M : ").split())
# matrix = []

# for i in range(N):
#     row = list(map(int, input("Enter the elements : ").split()))
#     matrix.append(row)

# arr = np.array(matrix)
# sum_value = np.sum(arr, axis=0)
# prod_value = np.prod(sum_value)

# print(prod_value)

# Min and Max

# import numpy

# my_array = numpy.array([[2, 5], [3, 7], [1, 3], [4, 0]])

# print(numpy.min(my_array, axis = 0))
# print(numpy.min(my_array, axis = 1))
# print(numpy.min(my_array, axis = None))
# print(numpy.min(my_array))

# print(numpy.max(my_array, axis = 0))
# print(numpy.max(my_array, axis = 1))
# print(numpy.max(my_array, axis = None))
# print(numpy.max(my_array))

# import numpy as np

# N, M = map(int, input("Enter the value of N and M : ").split())
# matrix = []

# for i in range(N):
#     row = list(map(int, input("Enter the elements : ").split()))
#     matrix.append(row)

# arr = np.array(matrix)
# min_values = np.min(arr, axis=1)
# max_min_value = np.max(min_values)

# print(max_min_value)

# Mean, Var and Std

# import numpy as np

# N, M = map(int, input("Enter the value of N and M : ").split())
# matrix = []

# for i in range(N):
#     row = list(map(int, input("Enter the elements : ").split()))
#     matrix.append(row)

# arr = np.array(matrix)

# print(np.mean(arr, axis = 1))
# print(np.var(arr, axis = 0))
# print(np.std(arr, axis = None))