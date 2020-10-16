def calculatesubgradient(mstGraph, numberOfNodes, lambdaV, sigmaV, yv):
    g = [0] * numberOfNodes

    v = 0
    while v < numberOfNodes:
        i = 0
        while i < numberOfNodes:
            sumXe = 0
            if mstGraph[v][i] > 0:
                sumXe += 1
            i += 1
        g[v] = sumXe - 2 - (sigmaV[v] * yv[v])
        v += 1
    
    return g