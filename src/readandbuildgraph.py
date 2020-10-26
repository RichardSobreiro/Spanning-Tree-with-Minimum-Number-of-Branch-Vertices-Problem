import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def buildgraph(path):
    file = open(path, "r")
    #G = nx.Graph()
    fileLines = file.readlines()
    lineCounter = 0
    incidenceMatrix = []
    numberOfNodes = 0
    for line in fileLines:
        if lineCounter == 0:
            lineSplited = line.split()
            incidenceMatrix = np.zeros((int(lineSplited[0]), int(lineSplited[0])))
            numberOfNodes = int(lineSplited[0])
            lineCounter += 1
            continue
        else:
            lineSplited = line.split()
            incidenceMatrix[(int(lineSplited[0]) - 1), (int(lineSplited[1]) - 1)] = 1
            incidenceMatrix[(int(lineSplited[1]) - 1), (int(lineSplited[0]) - 1)] = 1
            # G.add_nodes_from([lineSplited[0], lineSplited[1]])
            # edge = ([lineSplited[0], lineSplited[1]])
            # G.add_edge(*edge)
            lineCounter += 1
    
    #print("Nodes of graph: ")
    #print(G.nodes())
    #print("Edges of graph: ")
    #print(G.edges())
    #nx.draw_networkx(G)
    #plt.show()
    return incidenceMatrix, numberOfNodes