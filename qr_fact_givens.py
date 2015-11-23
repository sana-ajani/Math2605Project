import numpy as np
import math

def givens(R, a, b):
    i, j = a
    m, n = b
    base = R[i][j]
    second = R[m][n]

    if b != 0:
        cos = float(base) / math.sqrt(base**2 + second**2)
        sin = float(second) / math.sqrt(base**2 + second**2)


    identity = np.eye(A.shape[0])




def qr_fact_givens(A, b):
    copyA = np.copy(A)
    gList = []
    G = 0
    for y in range(copyA.shape[0]):
        columnList = copyA[:,y].tolist()
        counter = 0
        for num in columnList[y+1:copyA.shape[1]]:
            columnList = copyA[:,y].tolist()
            #print copyA
            base = columnList[y]
            #print base
            second = num
            if (num = 0):
                cos = 1
                sin = 0
            else:
                r = math.sqrt(base**2 + second**2)
                cos = float(base) / r
                sin = -1 * float(num) / r

                identity = eye(copyA.shape[0])
                identity[y, y] = cos
                identity[y + (counter+1), y] = sin
                #print "num =", num
                identity[y, y+(counter+1)] = -sin
                identity[y+(counter+1), y+counter+1] = cos
                counter += 1
                G = identity
                #print "G = ",G
                gList.append(identity)
                copyA = matrixMult(G, copyA)
    R = copyA
    Q = eye(A.shape[0])
    for g in gList:
        gT = g.transpose()
        Q = matrixMult(Q,gT)

    errorMatrix = matrixMult(Q,R) - A
    #print "error matrix =", errorMatrix
    maximum = 0
    for y in range(errorMatrix.shape[0]):
        for x in range(errorMatrix.shape[1]):
            if abs(errorMatrix[x,y]) > maximum:
                maximum = abs(errorMatrix[x,y])
    #print "max =", maximum
    x0 = solve_qr_b(Q, R, b)
    hErrorMatrix = matrixMult(A,x0) - b
    hxerror = 0
    for y in range(hErrorMatrix.shape[0]):
        for x in range(hErrorMatrix.shape[1]):
            if abs(hErrorMatrix[y,x]) > hxerror:
                hxerror = abs(hErrorMatrix[y,x])
    return Q, R, maximum, x0, hxerror
