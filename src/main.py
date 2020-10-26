import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

from readandbuildgraph import buildgraph
from stepone import calculatelambdav
from steptwo import calculatezlambdak, updatesigmav
from stepthree import calculatesubgradient
from stepfour import calculatestepsize
from stepfive import calculatelambdakplusone
from prim import Graph

def plotGraph(mstGraph, numberOfNodes, lb, ub, elapsedTime, nosBranch):
    G = nx.Graph()
    i = 0
    while i < numberOfNodes:
        j = 0
        while j < numberOfNodes:
            if mstGraph[i][j] > 0:
                edge = ([(i + 1), (j + 1)])
                G.add_edge(*edge)
            j += 1
        i += 1
    nx.draw_networkx(G)
    plt.title('LB = ' + str(lb) + '\nElapsedTime = ' + str(elapsedTime) + '\nNos Branch = ' + str(nosBranch))
    plt.show()

def main(argv):
    pathFileInstance = argv[0]
    zup = int(argv[1])
    #fileInstanceName = "Spd_RF2_20_27_211.txt"
    #path = "C:\\Users\\Richard Sobreiro\\source\\repos\\Spanning-Tree-with-Minimum-Number-of-Branch-Vertices-Problem\\MBV_Instances\\Spd_Inst_Rid_Final2\\" + fileInstanceName
    #zup = 1
    
    kmax = 1000
    k = 0
    lambdaV = []
    sigmaV = []
    zeur = sys.maxsize
    ek = 0.1

    start = time.time()

    adjacencyMatrix, numberOfNodes = buildgraph(pathFileInstance)
    
    # 1. Set λ_(v) = max_(u ∈ Vd) { δ1u }, ∀ v ∈ V′;k = 0
    lambdaV, sigmaV = calculatelambdav(adjacencyMatrix, len(adjacencyMatrix))
    mstGraph = adjacencyMatrix
    nosBranch = 0
    while k < kmax:
        # 2. Solve the Lagrangian relaxation by solving separately problems (3.4) and (3.5)
        # and obtain z(λ(k)) = −2Sumv∈V λv(k) + z1(λ(k)) + z2(λ(k)), and, also, (x(λ(k)),
        # y(λ(k))). Keep zEUR, the best solution value found so far.
        z, yv, nosBranch, mstGraph, sigmaV = calculatezlambdak(adjacencyMatrix, numberOfNodes, lambdaV, sigmaV)
        
        # print ('Nos Branchs = ' + str(nosBranch))
        # print ('Z = ' + str(z))
        # Keep zEUR, the best solution value found so far.
        if z < zeur and z > 0:
            zeur = z

        # 3. Calculate the subgradient g(k), whose v-th component is gv(k) = $e∈A(v) xe(λ(k))−
        # 2 − δvyv(λ(k))
        g = calculatesubgradient(mstGraph, numberOfNodes, lambdaV, sigmaV, yv)

        # 4. Calculate the stepsize tk: tk = ϵk * zEUR−z(λ(k))/∥g(k)∥^2
        t = calculatestepsize(zup, z, g, ek)

        # 5. Set λv(k+1)
        lambdaV = calculatelambdakplusone(lambdaV, sigmaV, t, g, numberOfNodes)

        # 6. If k ≥ kmax Stop else k = k + 1 and iterate.
        k += 1
    
    end = time.time()

    elapsedTime = end - start
    print("Elapsed Time = " + str(elapsedTime))
    print ('Nos Branchs = ' + str(nosBranch))
    print('Min Zeur = ' + str(zeur))
    plotGraph(mstGraph, numberOfNodes, zeur, zup, elapsedTime, nosBranch)
   
if __name__ == '__main__':
    main(sys.argv[1:])