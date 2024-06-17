# #ADDITION OF MATRIX
# A = [[1,3,5],
#      [2,4,6],
#      [7,9,11]]

# B = [[8,13,15],
#      [12,14,16],
#      [18,19,17]]

# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]

# for i in range(len(A)):
#     for j in range(len(A[0])):# A[0] represents column
#         result[i][j] = A[i][j] + B[i][j]
        
# for r in result:   
#     print(r)

#TRANSPOSE OF MATRIX
 
# A = [[1,3,5],
#      [2,4,6],
#      [7,9,11]]

# B = [[0,0,0],
#      [0,0,0],
#      [0,0,0]]

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         B[j][i] = A[i][j]
    
# for i in B:
#     print(i)

#LIST COMPREHENSION

# A = [[1,3,5],
#      [2,4,6],
#      [7,9,11]]

# B = [[A[j][i] for j in range(len(A[0]))] for i in range(len(A))]

# for i in B:
#      print(i)

#MULTIPLICATION OF TWO MATRICES

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[1,2,1,1],
     [4,2,1,2],
     [6,3,4,1]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
         for k in range(len(B)):
              result[i][j] =  result[i][j] + (A[i][k] * B[k][j])

for r in result:       
     print(r)
        

