import numpy as np
#from np.linalg import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import sys

from helper_methods import *

A = np.matrix([[0, 1.2, 1.1, .9, .1, 0, 0, 0, 0],
            [.7, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, .85, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, .9, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, .9, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, .88, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, .8, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, .77, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, .40, 0]])
## Test tolerance value
tol = 0.001
## Starting eigenvalue
initEig = np.array([[2.1],[1.9],[1.8],[2.1],[2.0],
                 [1.7],[1.2],[0.9],[0.5]])

def power_method(A, tol, initEig):
    return power_method_calculations(A, tol, initEig, initEig[0,0], 0)

#recursive power method function that performs all the calculations and increments an iterator
def power_method_calculations(matrixA, tol, initVect, initVal, num_iters):
    num_iters += 1
    if num_iters >= 100:
        return None
    result = np.dot(matrixA, initVect)
    nextVect = result / initVect[0,0]
    vect = initVect / initVal
    err = abs(find_max(nextVect) - find_max(vect))
    #check to see if the calculated tolerance is greater than the tolerance passed in
    if err > tol:
        return power_method_calculations(A, tol, result, initVect[0,0], num_iters)
    #if not, print the number of iterations, max eigenvalue, eigenvector
    print("number of iterations:", num_iters, "eigenvalue:", find_max(nextVect), "eigenvector:", nextVect)

power_method(A, tol, initEig)
