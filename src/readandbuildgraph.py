import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def buildgraph(path):
    file = open(path, "r")
    G = nx.Graph()
    fileLines = file.readlines()
    lineCounter = 0
    incidenceMatrix = []
    numberOfNodes = 0
    for line in fileLines:
        if lineCounter == 0:
            elements = line.split()
            incidenceMatrix = np.zeros((int(elements[1]), int(elements[1])))
            numberOfNodes = int(elements[1])
            lineCounter += 1
            continue
        else:
            elements = line.split()
            incidenceMatrix[int(elements[0]), int(elements[1])] = 1
            incidenceMatrix[int(elements[1]), int(elements[0])] = 1
            G.add_nodes_from([elements[0], elements[1]])
            edge = ([elements[0], elements[1]])
            G.add_edge(*edge)
            lineCounter += 1
    
    #print("Nodes of graph: ")
    #print(G.nodes())
    #print("Edges of graph: ")
    #print(G.edges())
    nx.draw_networkx(G)
    plt.show()
    return incidenceMatrix, numberOfNodes