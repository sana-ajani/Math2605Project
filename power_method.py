import numpy as np
#from np.linalg import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import sys

from helper_methods import *

#tol = 0.001
#starting eigenvalue
#initEig = np.array([[2.1],[1.9],[1.8],[2.1],[2.0],
            #    [1.7],[1.2],[0.9],[0.5]])

#find the max value in matrix
def find_max(A):
    B = A[0,0]
    for i in range (A.shape[0]):
        for j in range (A.shape[1]):
            if A[i,j] > B:
                B = A[i,j]
    return B

def power_method(matrixA, init_vect, tol = 0.0001, iter = 100):
    matrixA = np.array(matrixA)
    init_vect = np.array(init_vect)
    last_eig = 0
    result = np.dot(matrixA, init_vect)
    num_iter = 1

    current_eig = result.item(0)
    calcTol = abs(current_eig - last_eig)
    while calcTol > tol:
        last_eig = current_eig
        result = np.dot(matrixA, init_vect)
        current_eig = result[0]

        result = result / float(current_eig)
        init_vect = result
        num_iter += 1
        if num_iter > iter:
            return None
    print("Eigenvalue: ", current_eig)
    print("Eigenvector: ", result)
    print("Number of iterations: ", num_iter)

def main():

    matrix = []
    inverse_matrix = []
    e = 0.0005
    max_iter = 100

    data = []
    inverse_data = []

    while len(matrix) < 1000:
        matrix.append(create_matrix())

    for m in matrix:
        inverse_matrix.append(invert(m))

    for m in matrix:
        data.append(power_method(m, [1, 1], e, max_iter))

    for m in inverse_matrix:
        inverse_data.append(power_method(m, [1,1], e, max_iter))

    #First scatterplot
    plt.subplot(2, 1, 1)
    plt.scatter([m['det(A)'] for m in data],
                [m['trace(A)'] for m in data], c=[m['num of iterations'] for m in data], cmap=mpl.cm.gist_yarg)

    plt.title("Power method")
    plt.xlabel("Determinant")
    plt.ylabel("Trace")

    #Second scatterplot (inverse of matrix)
    plt.subplot(2, 1, 2)
    plt.scatter([m['det(A)'] for m in inverse_data],
                [m['trace(A)'] for m in inverse_data],
                c=[m['#iterations'] for m in inverse_data], cmap=mpl.cm.gray)

    plt.title("Power method for Inverse of Matrix")
    plt.xlabel("Determinant")
    plt.ylabel("Trace")

if __name__ == '__main__':
    #print power_method([[3,4],[3,1]], [1,1  ])
    print power_method([[0, 11, -5],[-2, 17, -7],[-4, 26, -10]], [1,1,1])
    print power_method([[1, 1, 0],[3, -1, 0],[0, 0, -2]], [1,1,1])

    main()
