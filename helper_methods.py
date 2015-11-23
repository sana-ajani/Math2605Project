import numpy as np
import random

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

    return ((1 / determinant(matrixA)) * np.array([[d, -b], [-c, a]]))


def trace(matrixA):
    return matrixA[0][0] + matrixA[1][1]

def create_matrix():
    matrix = create_random_matrix(-2, 2)
    if not determinant(matrix):
        return create_matrix()
    return matrix


def create_random_matrix(low, high):
    return [[random.uniform(low, high) for i in range(2)] for j in range(2)]

#find the max value in matrix
def find_max(A):
    B = A[0,0]
    for i in range (A.shape[0]):
        for j in range (A.shape[1]):
            if A[i,j] > B:
                B = A[i,j]
    return B
