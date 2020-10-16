def calculatelambdakplusone(lambdaV, sigmaV, t, g, numberOfnodes):
    lambdak = [0] * numberOfnodes
    v = 0
    while v < numberOfnodes:
        if (lambdaV[v] + (t * g[v])) < 0:
            lambdak = 0
        elif 0 <= (lambdaV[v] + (t * g[v])) <= (1/sigmaV[v]):
            lambdak = (lambdaV[v] + (t * g[v]))
        else:
            lambdak = (1/sigmaV[v])
        v += 1

    return lambdak