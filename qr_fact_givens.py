import numpy as np
import math
from numpy.linalg import qr
from helper_methods import *

def make_givens(R, a, b):
    i, j = a
    m, n = b
    base = R[i][j]
    val = R[m][n]

    if b != 0:
        cos = float(base) / math.sqrt(base ** 2 + val ** 2)
        sin = float(val) / math.sqrt(base ** 2 + val ** 2)

    return cos, sin


def qr_fact_givens(matrixA):
    Q = np.eye(matrixA.shape[0])
    R = matrixA
    for y in range(matrixA.shape[1]):
        for num in range(matrixA.shape[0]):
            if y is num:
                pivot_xy = (num, y)
            if y < num and R[num, y]:
                identity = np.eye(matrixA.shape[0])
                cos, sin = make_givens(R, pivot_xy, (num, y))
                identity[num][num] = cos
                identity[y][y] = cos
                identity[y][num] = sin
                identity[num][y] = -sin
                R = mult(identity, R)
                Q = Q.dot(identity.T)

    errorMatrix = mult(Q,R) - A
    maximum = find_max(errorMatrix)
    return Q, R, maximum

A = np.array([[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10], [1, 4, 10, 20]])
b = np.array([[1, 1/2, 1/3, 1/4]])
Q, R, maximum = qr_fact_givens(A)
print ("Q: ", Q)
print ("R ", R)
print("max", maximum)
