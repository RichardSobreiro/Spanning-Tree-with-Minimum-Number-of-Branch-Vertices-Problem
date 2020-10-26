import sys
import numpy as np

from prim import Graph

def calculatefirstterm(numberOfNodes, lambdaV, sigmaV):
    sumation = 0
    i = 0
    while i < numberOfNodes:
        if sigmaV[i] > 2:
            sumation += lambdaV[i]
        i += 1

    return -2 * sumation

def calculatesecondterm(mstGraph, numberOfNodes, lambdaV, sigmaV):
    z1 = 0
    v = 0
    while v < numberOfNodes:
        if sigmaV[v] > 2:
            j = 0   
            while j < numberOfNodes:
                if mstGraph[v][j] > 0:
                    z1 += lambdaV[v]
                j += 1
        v += 1

    return z1

def calculatethirdterm(numberOfNodes, lambdaV, sigmaV):
    v = 0
    y = numberOfNodes * [0]
    nosBranch = 0
    z2 = 0
    while v < numberOfNodes:
        if (1 - (sigmaV[v] * lambdaV[v])) <= 0:
            y[v] = 1
        else:
            y[v] = 0
        if sigmaV[v] > 2:
            nosBranch += 1
            z2 += y[v] * (1 - (sigmaV[v] * lambdaV[v]))
        v += 1
    
    return z2, y, nosBranch

def calculatezlambdak(adjacencyMatrix, numberOfNodes, lambdaV, sigmaV):
    g = Graph(numberOfNodes)
    i = 0
    wheightMatrix = np.zeros((numberOfNodes, numberOfNodes))
    while i < numberOfNodes:
        j = 0
        while j < numberOfNodes:
            if adjacencyMatrix[i][j] > 0:
                wheightMatrix[i][j] = lambdaV[i] + lambdaV[j]
            else:
                wheightMatrix[i][j] = sys.maxsize
            j += 1
        i += 1
    g.graph = wheightMatrix
    mstGraph = g.primMST(adjacencyMatrix)
    sigmaV = updatesigmav(mstGraph, numberOfNodes)

    firstTerm = calculatefirstterm(numberOfNodes, lambdaV, sigmaV)

    secondTerm = calculatesecondterm(mstGraph, numberOfNodes, lambdaV, sigmaV)

    thirdterm, yv, nosBranch = calculatethirdterm(numberOfNodes, lambdaV, sigmaV)

    z = firstTerm + secondTerm + thirdterm

    return z, yv, nosBranch, mstGraph, sigmaV

def updatesigmav(adjacencyMatrix, numberOfNodes):
    sigmaV = [0] * numberOfNodes
    i = 0
    while i < numberOfNodes:
        incidentEdgesAtNode = 0
        j = 0
        while j < numberOfNodes:
            if adjacencyMatrix[i][j] == 1:
                incidentEdgesAtNode += 1
            j += 1
        sigmaV[i] = incidentEdgesAtNode
        i += 1

    return sigmaV