import numpy as np
import math

def determinant(matrixA):
    a = matrixA[0][0]
    b = matrixA[0][1]
    c = matrixA[1][0]
    d = matrixA[1][1]
    return a * d - b * c


def invert(matrixA):
    a = matrixA[0][0]
    b = matrixA[0][1]
    c = matrixA[1][0]
    d = matrixA[1][1]
    inverse = np.array([[d, -b], [-c, a]])

    return ((1 / determinant(matrixA)) * inverse)


def trace(matrixA):
    return matrixA[0][0] + matrixA[1][1]


#find the max value in matrix
def find_max(A):
    B = A[0,0]
    for i in range (A.shape[0]):
        for j in range (A.shape[1]):
            if A[i,j] > B:
                B = A[i,j]
    return B

def norm(x):
    return math.sqrt(np.sum([x[i] ** 2 for i in range(len(x))]))

def mult(A, B):
    D = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            rows = A[i,:] #leftRows
            cols = B[:,j] #rightColumns
            c = np.dot(rows, cols)
            D[i,j] = c
    return D
