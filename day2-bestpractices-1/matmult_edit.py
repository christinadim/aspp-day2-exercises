# Program to multiply two matrices using nested loops
import random

# creates matrix

@profile
def matrix_creator(rows,columns):
    matrix = []
    for i in range(rows):
        matrix.append([random.randint(0,100) for r in range(columns)])
    return(matrix)

@profile
def multiplication_of_matrix(matrix1,matrix2):
    if len(matrix1) == len(matrix2):
        matrix3 = []
        for i in range(len(matrix1)):
            matrix3.append([random.randint(0,0) for r in range(len(matrix2[0]))])
        for i in range(len(matrix1)):
            # iterate through columns of Y
            for j in range(len(matrix2[0])):
                # iterate through rows of Y
                for k in range(len(matrix2)):
                    matrix3[i][j] += X[i][k] * Y[k][j]

    else:
        print("the columns of matrix1", len(matrix1)," are different from the rows of matrix2 ", len(matrix2))

    return(matrix3)
N = 250

# NxN matrix
X = matrix_creator(N,N)

# Nx(N+1) matrix
Y = matrix_creator(N,N+1)
result = multiplication_of_matrix(X,Y)

#print(result)
for r in result:
    print(r)
