import numpy as np
import math
from numpy.linalg import qr
from helper_methods import *
from solve_qr_b import *

def make_givens(R, a, b):
    i, j = a
    m, n = b
    val_a = R[i][j]
    val_b = R[m][n]

    if b is 0:
        c = 1
        s = 0
    else:
        r = math.sqrt(val_a**2 + val_b**2)
        c = val_a / r
        s = val_b / r
    return c, s


def qr_fact_givens(matrixA):
    m, n = matrixA.shape
    Q = np.eye(m)
    R = matrixA
    for i in range(n):
        for j in range(m):
            if i is j:
                pivot_xy = (j, i)
            if i < j and R[j, i]:
                G = np.eye(m)
                c,s = givens_rotation(R, pivot_xy, (j, i))
                G[j][j] = c
                G[i][i] = c
                G[i][j] = s
                G[j][i] = -s

                R = np.dot(G, R)
                Q = Q.dot(G.T)

    errorMatrix = mult(Q,R) - A
    maximum = find_max(errorMatrix)
    return Q, R, maximum

A = np.array([[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10], [1, 4, 10, 20]])
b = np.array([[1, 1/2, 1/3, 1/4]])
Q, R, maximum = qr_fact_givens(A)
print ("Q: ", Q)
print ("R ", R)
print("max", maximum)
