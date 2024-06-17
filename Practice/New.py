# nums = [4, 6, 9, 1, 11]
# square_all = map(lambda num : num ** 2, nums)
# print(square_all)

# print(20*10**2)

# var = set(['a', 'd'])
# var.union([1,2])
# var|([1,2])

# from itertools import *

# for i in zip(count(1), ['Bob', 'A', 'B']):
#     print(i)

# def addition(x,y):
#     return x + y

# num1 = [5,6,2]
# num2 = [7,1,4,9]

# result = map(addition,num1,num2)
# print(list(result))

# import os

# def getQueryResults(n, queries):
#     def power_of_two_array(n):
#         powers = []
#         power = 0
        
#         while n > 0:
#             if n % 2 == 1:
#                 powers.append(2 ** power)
#             power += 1
#             n //= 2
#         return powers
    
#     result = []
    
#     for query in queries:
#         l, r, m = query
#         powers = sorted(power_of_two_array(n))[l-1:r]
        
#         product_modulo_m = 1  # Initialize product_modulo_m before the loop
        
#         for p in powers:
#             product_modulo_m = (product_modulo_m * p) % m
        
#         result.append(product_modulo_m)
    
#     return result
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     queries_rows = int(input().strip())
#     queries_columns = int(input().strip())

#     queries = []

#     for _ in range(queries_rows):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = getQueryResults(n, queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()


# def pthFactor(n, p):
#     factors = []
    
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             factors.append(i)
#             if i != n // i:
#                 factors.append(n // i)
#     factors.sort()
               
#     if p <= len(factors):
#         return factors[p-1]
#     else:
#         return 0

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     p = int(input().strip())

#     result = pthFactor(n, p)

#     fptr.write(str(result) + '\n')

#     fptr.close()
