import sys
import numpy as np

class Graph():
    def __init__(self, numberOfNodes):
        self.V = numberOfNodes
        self.graph = np.zeros((self.V, self.V))

    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self, adjacencyMatrix):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V 

        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if adjacencyMatrix[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        #self.printMST(parent)
        mstGraph = np.zeros((self.V, self.V))
        v = 0
        while v < self.V:
            u = 0
            while u < self.V:
                if parent[v] == u:
                    mstGraph[u][v] = 1
                    mstGraph[v][u] = 1
                u += 1
            v += 1
        
        return mstGraph