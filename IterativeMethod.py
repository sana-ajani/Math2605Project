#Eduardo Mestanza

import numpy as np

#Iterative Method using Jacobi's Iterative Method

def jacobi_iter():
    num2 = float (2)
    num3 = float (3)
    num4 = float (4)

    aMatrix = np.array([[1, 1/num2, 1/num3], [1/num2, 1, 1/num4], [1/num3, 1/num4, 1]])
    bVector = np.array([0.1, 0.1, 0.1])
    xExact = np.array([9/float (190), 28/float (475), 33/float (475)])
    xApprox = np.array([0.0, 0.0, 0.0])
    numRandomVectors = 100

    e = 0.00005
    maximumIteration = 100
    enoughIteration = False

    for x in range(numRandomVectors):
        xVector = np.random.random((3,1))
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
        if (not enoughIteration):
            print("Need more Iterations!")

        else:
            print("Final Solution:", xVector)
            print(counter, " Iterations")
        print "Next example"
        for z in range (3):
            xApprox[z] += changedXVector[z]
    for y in range(3):
        xApprox[y] = xApprox[y] / float (numRandomVectors)
    print "Approximation Error:"
    print(xApprox - xExact)


#Iterative Method using Gauss-Seidel Iterative Method

def gs_iter():
    num2 = float (2)
    num3 = float (3)
    num4 = float (4)

    aMatrix = np.array([[1, 1/num2, 1/num3], [1/num2, 1, 1/num4], [1/num3, 1/num4, 1]])
    bVector = np.array([0.1, 0.1, 0.1])
    xExact = np.array([9/float (190), 28/float (475), 33/float (475)])
    xApprox = np.array([0.0, 0.0, 0.0])
    lowerSumVector = np.zeros_like(xApprox)
    upperSumVector = np.zeros_like(xApprox)
    numRandomVectors = 100

    e = 0.00005
    maximumIteration = 100
    enoughIteration = False
    for x in range(numRandomVectors):
        xVector = np.random.random((3,1))
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
        if (not enoughIteration):
            print("Need more Iterations!")

        else:
            print("Final Solution:", xVector)
            print(counter, " Iterations")
        print "Next example"
        for z in range (3):
            xApprox[z] += changedXVector[z]
    for y in range(3):
        xApprox[y] = xApprox[y] / float (numRandomVectors)
    print "Approximation Error:"
    print(xApprox - xExact)

gs_iter()