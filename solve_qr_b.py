import numpy as np
import math
from helper_methods import *

def solve_qr_b(Q, R, b):
    d = mult(Q.transpose(), b)
    #Rx = d
    x = Q.shape[0] - 1
    x_vect = zeros((R.shape[0], 1))
    sum_values = 0
    current = 0
    for i in xrange(R.shape[0] - 1, -1, -1):
        for j in xrange(R.shape[0] - 1, -1, -1):
            if (i == Q.shape[0] - 1):
                x_vect[i,0] = d[i,0] / R[R.shape[0] - 1, R.shape[1] - 1]
            else:
                if j > i:
                    sum_values = R[i,j] * x_vect[j,0] + sum_values
                elif j == i:
                    current = R[i,j]
                    x_vect[i,0] = (d[i,0] - sum_values) / current
                    break

    return x
