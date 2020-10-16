def calculatelambdav(incidenceMatrix, numberOfNodes):
    lambdaV = [numberOfNodes]
    sigmaV = [numberOfNodes]
    i = 0
    while i < numberOfNodes:
        incidentEdgesAtNode = 0
        j = 0
        while j < numberOfNodes:
            if incidenceMatrix[i][j] == 1:
                incidentEdgesAtNode += 1
            j += 1
        if incidentEdgesAtNode > 2:
            sigmaV[i] = incidentEdgesAtNode
        else:
            sigmaV[i] = 0
        i += 1

    i = 0
    while i < numberOfNodes:
        if sigmaV[i] > 0:
            lambdaV = 1/sigmaV[i] 
        else:
            lambdaV = 0
        i += 1

    return [lambdaV, sigmaV]