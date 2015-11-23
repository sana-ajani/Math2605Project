import numpy as np
import math

def givens(R, a, b):
    i, j = a
    m, n = b
    base = R[i][j]
    second = R[m][n]

    if b != 0:
        cos = float(base) / math.sqrt(base**2 + second**2)
        sin = float(second) / math.sqrt(base**2 + second**2)

    else:
        cos = 1
        sin = 0
    return cos, sin

    identity = np.eye(A.shape[0])


def qr_fact_givens(matrixA):
    copyA = np.copy(matrixA)
    m = copyA.shape[0]
    n = copyA.shape[1]
    Q = np.eye(m)
    R = copyA
    gList = []
    G = 0
    for i in range(m):
        for j in range(n):
            if i is j:
                pivot_xy = (j, i)
            if i < j and R[j, i]:
                identity = np.eye(m)
                cos, sin = givens(R, pivot_xy, (j, i))
                identity[j][j] = cos
                identity[i][i] = cos
                identity[i][j] = sin
                identity[j][i] = -sin
                G = identity
                gList.append(identity)
                R = np.dot(identity, R)
    for g in gList:
        gT = g.transpose()
        Q = np.dot(Q,gT)

    return Q, R
