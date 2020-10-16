from prim import prim

def calculatefirstterm(numberOfNodes, lambdaV):
    sumation = 0
    i = 0
    while i < numberOfNodes:
        sumation += lambdaV
        i += 1

    return -2 * sumation

def calculatesecondterm(incidenceMatrix, lambdaV, numberOfNodes):
    mstGraph = prim(incidenceMatrix, lambdaV, numberOfNodes)
    z1 = 0
    v = 0
    while v < numberOfNodes:
        j = 0
        while j < numberOfNodes:
            if mstGraph[v][j] > 0:
                z1 += lambdaV[v]
            j += 1
        v += 1

    return z1, mstGraph

def calculatethirdterm(incidenceMatrix, numberOfNodes, lambdaV, sigmaV):
    v = 0
    y = numberOfNodes * [0]
    z2 = 0
    while v < numberOfNodes:
        if (1 - (sigmaV[v] * lambdaV[v])) <= 0:
            y[v] = 0
        z2 += y[v] * (1 - (sigmaV[v] * lambdaV[v]))
        v += 1
    
    return z2, y

def calculatezlambdak(incidenceMatrix, numberOfNodes, lambdaV, sigmaV):
    firstTerm = calculatefirstterm(numberOfNodes, lambdaV)

    secondTerm, mstGraph = calculatesecondterm(incidenceMatrix, lambdaV, numberOfNodes)

    thirdterm, y = calculatethirdterm(incidenceMatrix, numberOfNodes, lambdaV, sigmaV)

    z = firstTerm + secondTerm + thirdterm

    return z, mstGraph, y