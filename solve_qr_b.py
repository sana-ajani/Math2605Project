import numpy as np
import math
from helper_methods import *

def solve_qr_b(Q, R, b):
    d = mult(Q, b)
    #Rx = d
    x = Q.shape[0] - 1
    x_vect = zeros((R.shape[0], 1))
    sum_values = 0

    while (x >= 0):
        if (x == Q.shape[0] - 1):
                x[i,0] = d[i,0] / R[R.shape[0] - 1, R.shape[1] - 1]
        sum_values =


    x = np.zeros((R.shape[0]), 1)
    for i in xrange(R.shape[0] - 1, -1, -1):
        added = 0
        current = 0
        for j in xrange (R.shape[1] - 1, -1, -1):
            if i == Q.shape[0] - 1:
                x[i,0] = d[i,0] / R[R.shape[0] - 1, R.shape[1] - 1]
            else:
                if j > i:
                    added = R[i,j] * x[j,0] + added
                elif j == i:
                    current = R[i,j]
                    x[i,0] = (y[i,0] - added) / current
                    break
    return x
