#Eduardo Mestanza

import numpy as np
import math
import csv

print "Running the LU Decomposition's main method: {}".format(__name__)

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
    errorMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[0]), dtype = "float64")

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


    # multiplies the L and U matrix together
    for i in range(pascalMatrix.shape[0]):
        for j in range(pascalMatrix.shape[1]):
            luMatrix[i, j] = np.dot(lMatrix[i, :], uMatrix[:, j])



    # Finds the error of ||LU - A||
    errorMatrix = luMatrix - pascalMatrix

    for i in range(errorMatrix.shape[0]):
        for j in range(errorMatrix.shape[1]):
            if (errorValue < errorMatrix[i, j]):
                errorValue = errorMatrix[i, j]

    print "Here we have the L matrix"
    print lMatrix
    print "Here we have the U matrix"
    print uMatrix
    print "Here we have the Error value ||LU - A||"
    print errorValue
    return lMatrix, uMatrix

def solve_lu_b(pascalMatrix):

    lSolMatrix, uSolMatrix = lu_fact(pascalMatrix)

    xVector = np.zeros((1, pascalMatrix.shape[0]), dtype = "float64")
    yVector = np.zeros((1, pascalMatrix.shape[0]), dtype = "float64")
    errorVector = np.zeros((1, pascalMatrix.shape[0]), dtype = "float64")
    bVector = np.zeros((1, pascalMatrix.shape[0]))
    pxVector = np.zeros((1, pascalMatrix.shape[0]), dtype = "float64")

    lMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]), dtype = "float64")
    uMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]), dtype = "float64")
    errorMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]), dtype = "float64")
    luSolMatrix = np.zeros((pascalMatrix.shape[0], pascalMatrix.shape[1]), dtype = "float64")

    x = pascalMatrix.shape[0] - 1
    y = pascalMatrix.shape[1] - 1
    pxError = 0
    errorValue = 0
    counter = 0
    sumValues = 0



    # put all elements of lSolMatrix into lMatrix, so we have a copy of the l matrix
    # done in lu_fact for future use
    for i in range(pascalMatrix.shape[0]):
        for j in range(pascalMatrix.shape[1]):
            uMatrix[i, j] = uSolMatrix[i, j]


    # do the same for uSolMatrix into uMatrix
    for i in range(pascalMatrix.shape[0]):
        for j in range(pascalMatrix.shape[1]):
            lMatrix[i, j] = lSolMatrix[i, j]

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




    # Calculates the error of ||LU - P||
    for i in range(pascalMatrix.shape[0]):
        for j in range(pascalMatrix.shape[1]):
            luSolMatrix[i, j] = np.dot(lMatrix[i, :], uMatrix[:, j])
    errorMatrix = luSolMatrix - pascalMatrix       

    for i in range(errorMatrix.shape[0]):
        for j in range(errorMatrix.shape[1]):
            if (errorValue < errorMatrix[i, j]):
                errorValue = errorMatrix[i, j]

    # Calculates the error of ||Px - b||
    for i in range(pascalMatrix.shape[0]):
        pxVector[0, i] = np.dot(luSolMatrix[i, :], xVector[0, :])

    errorVector = pxVector - bVector

    for i in range(pxVector.shape[1]):
        pxError += ((errorVector[0, i]) ** 2)
    pxError = math.sqrt(pxError)

    with open("LU-Decomposition results.csv", "a") as LUFile:
        LUFileWriter = csv.writer(LUFile)
        LUFileWriter.writerow([pascalMatrix.shape[0], errorValue, pxError])

    LUFile.close()


    print "Here is the solution to the Px = b where x is:"
    print xVector
    print "Here is the error value of ||LU - P||"
    print errorValue
    print "Here is the error value of ||Px - b||"
    print pxError

def main():

    with open("LU-Decomposition results.csv", "a") as LUFile:
        LUFileWriter = csv.writer(LUFile)
        LUFileWriter.writerow(["Dimension of Pascal Matrix", "||LU - P|| Error", "||Px - b|| Error"])

    LUFile.close()

    n = 12

    pascalMatrix = np.zeros((0, 0), dtype = "float64")
    lMatrix = np.zeros((0, 0))
    uMatrix = np.zeros((0, 0))

    for i in range(n):
        print ("Pascal Matrix of dimension: ", i)
        solve_lu_b(pascal_matrix(i + 1))

if __name__ == '__main__':
    main()