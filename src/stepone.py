def calculatelambdav(adjacencyMatrix, numberOfNodes):
    oneOverSigmaV = [0] * numberOfNodes
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

    v = 0
    while v < numberOfNodes:
        if sigmaV[v] > 0:
            oneOverSigmaV[v] = 1/sigmaV[v] 
        else:
            oneOverSigmaV[v] = 0
        v += 1

    v = 0
    lambdaV = [0] * numberOfNodes
    while v < numberOfNodes:
        if sigmaV[v] > 2:
            maxOneOverSigmaU = 0    
            u = 0
            while u < numberOfNodes:
                if oneOverSigmaV[u] > maxOneOverSigmaU and adjacencyMatrix[v][u] > 0:
                    maxOneOverSigmaU = oneOverSigmaV[u]
                u += 1
            lambdaV[v] = maxOneOverSigmaU
        v += 1

    while v < numberOfNodes:
        if sigmaV[v] <= 2:
            lambdaV[v] = 0
        v += 1

    return [lambdaV, sigmaV]