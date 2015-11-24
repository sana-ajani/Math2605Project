#Eduardo Mestanza

import numpy as np
import math

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

def lu_fact():

    pascalMatrix = pascal_matrix(4)

    lMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]),dtype='float64') 
    uMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]),dtype='float64')

    maxPascalVector = np.zeros((1,pascalMatrix.shape[1]))
    maxLVector = np.zeros((1, pascalMatrix.shape[1]))
    maxUVector = np.zeros((1, pascalMatrix.shape[1]))

    maxLValue = 0
    maxUValue = 0
    maxPascalValue = 0
    sumOfCollumn = 0

    # This nested for loops adds all of the values of the pascal matrix
    # into the U Matrix, that way we can have an untouched pascal matrix and
    # use U to work the math.
    for i in range(pascalMatrix.shape[0]):
        for j in range(pascalMatrix.shape[1]):
            uMatrix[i, j] = pascalMatrix[i, j]

    # Adds one to the diagonal of the L Matrix
    for i in range(pascalMatrix.shape[0]):
        lMatrix[i, i] = 1

    # This nested for loop does the L, U decomposition, first it makes every
    # element under the diagonal in the L matrix equal to the value of the pascal
    # matrix value at that position divided by 
    for i in range(pascalMatrix.shape[1] - 1):
        for j in range(i+1, pascalMatrix.shape[0]):
            lMatrix[j,i] = uMatrix[j,i] / uMatrix[i,i]
            uMatrix[j,i:] = uMatrix[j,i:] - (lMatrix[j,i] * uMatrix[i,i:])
            uMatrix[j,i] = 0

    for i in range(pascalMatrix.shape[1]):
        for j in range(pascalMatrix.shape[1]):
            sumOfCollumn += abs(pascalMatrix[j, i])
        maxPascalVector[0, i] = sumOfCollumn
        sumOfCollumn = 0

    for i in range(maxPascalVector.shape[1]):
        if (maxPascalVector[0, i] > maxPascalValue):
            maxPascalValue = maxPascalVector[0, i]

    for i in range(lMatrix.shape[1]):
        for j in range(lMatrix.shape[1]):
            sumOfCollumn += abs(lMatrix[j, i])
        maxLVector[0, i] = sumOfCollumn
        sumOfCollumn = 0

    for i in range(maxLVector.shape[1]):
        if (maxLVector[0, i] > maxLValue):
            maxLValue = maxLVector[0, i]

    for i in range(lMatrix.shape[1]):
        for j in range(lMatrix.shape[1]):
            sumOfCollumn += abs(lMatrix[j, i])
        maxLVector[0, i] = sumOfCollumn
        sumOfCollumn = 0

    for i in range(maxLVector.shape[1]):
        if (maxLVector[0, i] > maxLValue):
            maxLValue = maxLVector[0, i]

    print pascalMatrix
    print uMatrix
    print lMatrix

lu_fact()