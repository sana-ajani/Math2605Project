#Eduardo Mestanza

import numpy as np
import math
import csv

#Iterative Method using Jacobi's Iterative Method

def jacobi_iter(xVector, e, maximumIteration):

    num2 = float (2)
    num3 = float (3)
    num4 = float (4)

    aMatrix = np.array([[1, 1/num2, 1/num3], [1/num2, 1, 1/num4], [1/num3, 1/num4, 1]])

    bVector = np.array([0.1, 0.1, 0.1])
    xExact = np.array([9/float (190), 28/float (475), 33/float (475)])
    xApprox = np.array([0.0, 0.0, 0.0])


    errorVector = np.zeros((1, aMatrix.shape[1]), dtype = "float64")
    errorApprox = 0
    numRandomVectors = 100

    enoughIteration = False


    with open("Jacobi Method results", "w") as iterationFile:
        iterationFileWriter = csv.writer(iterationFile)
        
    iterationFile.close()

    for x in range(numRandomVectors):
        xVector = np.random.random((3,1))
        # Here we write the xVector into the csv file
        with open("Jacobi Method results", "a") as iterationFile:
            iterationFileWriter = csv.writer(iterationFile)
            iterationFileWriter.writerow([xVector])
        iterationFile.close()
        for i in range(maximumIteration):
            counter = i
            changedXVector = np.zeros_like(xVector)
            dMatrix = np.zeros_like(aMatrix)
            for j in range(3):
                dMatrix[j, j] = 1 / aMatrix[j, j]
                upperSum = np.dot(aMatrix[j, j + 1:], xVector[j + 1:])
                lowerSum = np.dot(aMatrix[j, :j], xVector[:j])
                changedXVector[j] = dMatrix[j, j]*((bVector[j]) - (upperSum + lowerSum))

            if np.allclose(xVector, changedXVector, e):
                enoughIteration = True
                break
            xVector = changedXVector
        for z in range (3):
            xApprox[z] += changedXVector[z]
        if (not enoughIteration):
            print("Need more Iterations!")
        else:
            # Here write the number of iterations and approximation
            continue
    for y in range(3):
        xApprox[y] = xApprox[y] / float (numRandomVectors)

    errorVector = xApprox - xExact

    for i in range(errorVector.shape[0]):
        errorApprox += ((errorVector[i]) ** 2)
    errorApprox = math.sqrt(errorApprox)

    print "Jacobi iteration:"
    print "Solution from the last randomly generated x Vector:"
    print xVector
    print(counter, " Iterations")
    print ("Error Aprroximation", errorApprox)

#Iterative Method using Gauss-Seidel Iterative Method

def gs_iter(xVector, e, maximumIteration):

    num2 = float (2)
    num3 = float (3)
    num4 = float (4)

    aMatrix = np.array([[1, 1/num2, 1/num3], [1/num2, 1, 1/num4], [1/num3, 1/num4, 1]])

    bVector = np.array([0.1, 0.1, 0.1])
    xExact = np.array([9/float (190), 28/float (475), 33/float (475)])
    xApprox = np.array([0.0, 0.0, 0.0])
    errorVector = np.zeros((1, aMatrix.shape[1]), dtype = "float64")


    errorApprox = 0
    lowerSumVector = np.zeros_like(xApprox)
    upperSumVector = np.zeros_like(xApprox)
    numRandomVectors = 100

    enoughIteration = False

    with open("Gauss-Seidel Method results", "w") as iterationFile:
        iterationFileWriter = csv.writer(iterationFile)

    iterationFile.close()

    for x in range(numRandomVectors):
        xVector = np.random.random((3,1))
        # Here we write the xVector into the csv file
        with open("Gauss-Seidel Method results", "a") as iterationFile:
            iterationFileWriter = csv.writer(iterationFile)
            iterationFileWriter.writerow([xVector])
        iterationFile.close()

        for i in range(maximumIteration):
            counter = i
            changedXVector = np.zeros_like(xVector)
            dMatrix = np.zeros_like(aMatrix)

            for k in range(3):
                dMatrix[k, k] = 1 / aMatrix[k, k]

            dMatrix[1, 0] = -1 * (aMatrix[1, 0] / (aMatrix[0, 0] * aMatrix[1, 1]))
            dMatrix[2, 1] = -1 * (aMatrix[2, 1] / (aMatrix[1, 1] * aMatrix[2, 2]))
            dMatrix[2, 0] = (-1 * aMatrix[1, 1] * aMatrix[2, 0]) + (aMatrix[1, 0] * aMatrix[2, 1])
            dMatrix[2, 0] = (dMatrix[2, 0] / (aMatrix[0, 0] * aMatrix[1, 1] * aMatrix[2, 2]))

            for j in range(3):
                upperSumVector[j] = np.dot(aMatrix[j, j + 1:], xVector[j + 1:])
                changedXVector[j] = np.dot(dMatrix[j, :], (bVector - upperSumVector))

            if np.allclose(xVector, changedXVector, e):
                enoughIteration = True
                break
            xVector = changedXVector
        for z in range (3):
            xApprox[z] += changedXVector[z]
        if (not enoughIteration):
            print("Need more Iterations!")
        else:
            # Here write the number of iterations and approximation
            continue
    for y in range(3):
        xApprox[y] = xApprox[y] / float (numRandomVectors)

    errorVector = xApprox - xExact

    for i in range(errorVector.shape[0]):
        errorApprox += ((errorVector[i]) ** 2)
    errorApprox = math.sqrt(errorApprox)

    print "Gauss-Seidel Iteration"
    print "Solution from the last randomly generated x Vector:"
    print xVector
    print(counter, " Iterations")
    print ("Error Aprroximation", errorApprox)




def main():
    num2 = float (2)
    num3 = float (3)
    num4 = float (4)

    aMatrix = np.array([[1, 1/num2, 1/num3], [1/num2, 1, 1/num4], [1/num3, 1/num4, 1]])

    xVector = np.zeros((3,1))

    e = 0.00005
    maximumIteration = 100

    jacobi_iter(xVector, e, maximumIteration)
    gs_iter(xVector, e, maximumIteration)

if __name__ == '__main__':
    main()