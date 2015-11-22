import numpy as np
from numpy.linalg import *
import matplotlib as mpl
import matplotlib
import random
import sys

from helper_methods import *

#Test tolerance value
tol = 0.001

#Starting eigenvalue
initEig = array([[2.1],[1.9],[1.8],[2.1],[2.0],
                 [1.7],[1.2],[0.9],[0.5]])

#Finds the maximum value in a matrix/vector
def find_max(A):
    B = A[0,0]
    for i in range (A.shape[0]):
        for j in range (A.shape[1]):
            if A[i,j] > B:
                B = A[i,j]
    return B


def power_method(matrixA, init_vect, tol, iter):
    matrixA = numpy.array(matrixA)
    init_vect = numpy.array(init_vect)
    last_eig = 0
    result = np.dot(matrixA, initVect)
    num_iter = 1

    current_eig = result[0]
    calcTol = abs(current_eig - last_eig)
    while calcTol > tol:
        last_eig = current_eig
        result = np.dot(matrixA, init_vect)
        current_eig = result[0]

        result = result / float(current_eig)
        init_vect = result
        num_iter = num_iter + 1
        if num_iter > iter:
            return None
    return {
        "eigenvalue: ": current_eig,
        "eigenvector: ": result,
        "number of iterations: " num_iter
    }

def main():

    matrix = []

    while len(matrix) < 1000:
        matrix.append(create_matrix())

    inverted_matrix = [invert(m) for m in matrices]

    data = []
