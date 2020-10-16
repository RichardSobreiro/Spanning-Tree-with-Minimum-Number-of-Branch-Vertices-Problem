import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from readandbuildgraph import buildgraph
from stepone_calculatelambdav import calculatelambdav
from steptwo_calculatezlambdak import calculatezlambdak
from stepthree_calculatesubgradient import calculatesubgradient
from stepfour_calculatestepsize import calculatestepsize
from stepfive_calculatelambdakplusone import calculatelambdakplusone

def main():
    path = "C:\\Users\\Richard Sobreiro\\source\\repos\\Spanning-Tree-with-Minimum-Number-of-Branch-Vertices-Problem\\MBV_Instances\\Spd_Inst_Rid_Final2\\Spd_RF2_20_27_211.txt"
    kmax = 10

    k = 0
    lambdaV = []
    sigmaV = []
    zeur = sys.maxsize
    ek = 0.002

    incidenceMatrix, numberOfNodes = buildgraph(path)

    currentIncidenceMatrix = incidenceMatrix

    while k < kmax:
        # 1. Set λ_(v) = max_(u ∈ Vd) { δ1u }, ∀ v ∈ V′;k = 0
        lambdaV, sigmaV = calculatelambdav(currentIncidenceMatrix, len(incidenceMatrix))

        # 2. Solve the Lagrangian relaxation by solving separately problems (3.4) and (3.5)
        # and obtain z(λ(k)) = −2Sumv∈V λv(k) + z1(λ(k)) + z2(λ(k)), and, also, (x(λ(k)),
        # y(λ(k))). Keep zEUR, the best solution value found so far.
        z, mstGraph, y = calculatezlambdak(incidenceMatrix, numberOfNodes, lambdaV, sigmaV)

        # 3. Calculate the subgradient g(k), whose v-th component is gv(k) = $e∈A(v) xe(λ(k))−
        # 2 − δvyv(λ(k))
        g = calculatesubgradient(mstGraph, numberOfNodes, lambdaV, sigmaV, y)

        # 4. Calculate the stepsize tk: tk = ϵk * zEUR−z(λ(k))/∥g(k)∥^2
        t = calculatestepsize(zeur, z, g, ek)

        # 5. Set λv(k+1)
        lambdak = calculatelambdakplusone(lambdaV, sigmaV, t, g, numberOfNodes)

        # 6. If k ≥ kmax Stop else k = k + 1 and iterate.
        k += 1
   
if __name__ == '__main__':
    main()