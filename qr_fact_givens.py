import numpy as np
import math
from helper_methods import *
from solve_qr_b import *


def make_givens(R, a, b):
    #a and b will be tuples (x, y)
    i, j = a
    m, n = b
    base = R[i][j]
    val = R[m][n]

    if b != 0:
        cosX = float(base) / math.sqrt(base ** 2 + val ** 2)
        sinX = float(val) / math.sqrt(base ** 2 + val ** 2)

    return cosX, sinX


def qr_fact_givens(matrixA):
    Q = np.eye(matrixA.shape[0])
    R = matrixA
    for y in range(matrixA.shape[1]):
        for num in range(matrixA.shape[0]):
            if y is num:
                pivot = (num, y)
            if y < num:
                identity = np.eye(matrixA.shape[0])
                cosX, sinX = make_givens(R, pivot, (num, y))
                identity[num][num] = cosX
                identity[y][y] = cosX
                identity[y][num] = sinX
                identity[num][y] = -sinX
                R = mult(identity, R)
                Q = Q.dot(identity.T)

    #error value of ||QR - A||
    errorValue = 0
    errorMatrix = mult(Q,R) - A
    for i in range(errorMatrix.shape[0]):
        for j in range(errorMatrix.shape[1]):
            if (errorValue < errorMatrix[i, j]):
                errorValue = errorMatrix[i, j]

    x = solve_qr_b(Q, R, b)
    return Q, R, errorValue, x

A = np.array([[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10], [1, 4, 10, 20]])
b = np.array([[1, 1/2, 1/3, 1/4]])
Q, R, errorValue, x = qr_fact_givens(A)
print ("Q: ", Q)
print ("R ", R)
print ("the error ||QR - A||", errorValue)
print ('solution to Ax = b', x)
#print("x0:", x0)
