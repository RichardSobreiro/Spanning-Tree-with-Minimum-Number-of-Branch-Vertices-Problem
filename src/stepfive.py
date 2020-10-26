def calculatelambdakplusone(lambdaV, sigmaV, t, g, numberOfnodes):
    lambdakPlusOne = [0] * numberOfnodes
    v = 0
    while v < numberOfnodes:
        if (lambdaV[v] + (t * g[v])) < 0:
            lambdakPlusOne[v] = 0
        elif 0 <= (lambdaV[v] + (t * g[v])) <= (1/sigmaV[v]):
            lambdakPlusOne[v] = (lambdaV[v] + (t * g[v]))
        else:
            lambdakPlusOne[v] = (1/sigmaV[v])
        v += 1

    return lambdakPlusOne