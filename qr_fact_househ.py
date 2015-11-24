import numpy as np
import math
from helper_methods import *
from solve_qr_b import *

def make_h(c):
    height = len(c)
    mat = np.eye(height, 1)
    I = np.eye(height)

    #zip returns an iterator of tuples -- same as transposing it
    v = np.array([x + y for x, y in zip(c, norm(c) * mat)])
    u = v / norm(v)
    H = I - (2 * u * u.T)
    return H

def qr_fact_househ(matrixA):
    m = matrixA.shape[0]
    n = matrixA.shape[1]

    #get Householder vector for first column of A
    H = make_h(matrixA.T[0])
    Q = H

    for i in range(n):
        result = np.dot(Q, matrixA)
        result = result.T
        col = result[i, i:]
        smaller_matrix = make_h(col)
        height_1 = len(col)
        I = np.eye(n)

        #reverse all the H and V entries in matrix
        reverse = np.flipud(np.fliplr(smaller_matrix))

        #want to insert smaller_matrix into H2 (matrix of zeros)
        for r in range(reverse.shape[0]):
            for c in range(reverse.shape[1]):
                I[I.shape[0] - r - 1, I.shape[1] - c - 1] = reverse[r, c]

        Q = np.dot(I, Q)

    R = np.dot(Q, matrixA)

    return Q.T, R

A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
Q, R = qr_fact_househ(A)
print ("Q: ", Q)
print ("R ", R)
