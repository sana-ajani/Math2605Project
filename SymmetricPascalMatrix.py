#Eduardo Mestanza

import numpy as np
import math

pascalMatrix = np.zeros((0, 0), dtype = "float64")
lMatrix = np.zeros((0, 0))
uMatrix = np.zeros((0, 0))


def pascal_matrix(numDimensions):
    pascalMatrix = np.zeros((numDimensions, numDimensions))
    for i in range(numDimensions):
        if (i == 0):
            pascalMatrix[i, i:] = 1
            pascalMatrix[i:, i] = 1
        else:
            for j in range(numDimensions -1):
                pascalMatrix[i, j + 1] = pascalMatrix[i - 1, j + 1] + pascalMatrix[i, j]
    return pascalMatrix

def lu_fact(pascalMatrix):

    lMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]), dtype = "float64") 
    uMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]), dtype = "float64")
    luMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]), dtype = "float64")

    sumOfCollumn = 0
    errorValue = 0

    # This nested for loops adds all of the values of the pascal matrix
    # into the U Matrix, that way we can have an untouched pascal matrix and
    # use U to work the math.
    for i in range(pascalMatrix.shape[0]):
        for j in range(pascalMatrix.shape[1]):
            uMatrix[i, j] = pascalMatrix[i, j]

    # Adds one to the diagonal of the L Matrix
    for i in range(pascalMatrix.shape[0]):
        lMatrix[i, i] = 1

    # This nested for loop does the L, U decomposition
    for i in range(pascalMatrix.shape[1] - 1):
        for j in range(i+1, pascalMatrix.shape[0]):
            lMatrix[j,i] = uMatrix[j,i] / uMatrix[i,i]
            uMatrix[j,i:] = uMatrix[j,i:] - (lMatrix[j,i] * uMatrix[i,i:])
            uMatrix[j,i] = 0


    for i in range(pascalMatrix.shape[0]):
        for j in range(pascalMatrix.shape[1]):
            luMatrix[i, j] = np.dot(lMatrix[i, :], uMatrix[:, j])

    print pascalMatrix
    print lMatrix
    print uMatrix
    print luMatrix
    return lMatrix, uMatrix

def solve_lu_b(pascalMatrix):

    lSolMatrix, uSolMatrix = lu_fact(pascalMatrix)

    xVector = np.zeros((1, pascalMatrix.shape[0]), dtype = "float64")
    yVector = np.zeros((1, pascalMatrix.shape[0]), dtype = "float64")
    bVector = np.zeros((1,pascalMatrix.shape[0]))
    x = pascalMatrix.shape[0] - 1
    y = pascalMatrix.shape[1] - 1
    counter = 0
    sumValues = 0

    # Makes a b vector whose entries are (1, 1/2, 1/3 .... 1/n)
    for i in range(bVector.shape[1]):
        bVector[0, i] = 1/ float (i + 1)

    # Makes the solution for Ly = b
    for i in range(pascalMatrix.shape[0]):
        if (i == 0):
            yVector[0, i] = lSolMatrix[i, i]
        sumValues = bVector[0, i]
        for j in range(counter):
            lSolMatrix[i, j] = yVector[0, j] * lSolMatrix[i, j]
            sumValues -= lSolMatrix[i, j]
        yVector[0, i] = sumValues
        counter += 1
    print yVector

    counter = 0
    sumValues = 0

    # Makes the solution for Ux = y
    while (x >= 0):
        if (x == pascalMatrix.shape[0] - 1):
            xVector[0, x] = uSolMatrix[x, x]
        sumValues = yVector[0, x]
        j = pascalMatrix.shape[1] - 1
        while ((y < (pascalMatrix.shape[1] - 1)) and j > y):
            uSolMatrix[x, j] = xVector[0, j] * uSolMatrix[x, j]
            sumValues -= uSolMatrix[x, j]
            j -= 1
        xVector[0, x] = sumValues
        y -= 1
        x -= 1
    print xVector

solve_lu_b(pascal_matrix(4))