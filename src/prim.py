import sys
import numpy as np

def printMST(incidenceMatrix, numberOfNodes, parent):
    print("Edge \tWeight")
    for i in range(1, numberOfNodes):
        print (parent[i], "-", i, "\t", incidenceMatrix[i][ parent[i] ])

def minKey(incidenceMatrix, key, mstSet, numberOfNodes):
    min = sys.maxsize
    for v in range(numberOfNodes):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    return min_index

def prim(incidenceMatrix, weights, numberOfNodes):
    mstGraph = np.zeros(numberOfNodes, numberOfNodes)
    key = [sys.maxsize] * numberOfNodes
    parent = [None] * numberOfNodes

    key[0] = 0
    mstSet = [False] * numberOfNodes

    parent[0] = -1

    for cout in range(numberOfNodes):
        u = minKey(incidenceMatrix, key, mstSet, numberOfNodes)

        mstSet[u] = True

        for v in range(numberOfNodes):
            if incidenceMatrix[u][v] > 0 and mstSet[v] == False: #and key[v] > incidenceMatrix[u][v]:
                key[v] = weights[u] + weights[v]
                parent[v] = u
                mstGraph[u][v] = 1
                mstGraph[v][u] = 1
    
    return mstGraph

    

