from numpy import linalg as LA

def calculatestepsize(zeur, z, g, ek):
    t = ek * ((zeur - z)/ pow(LA.norm(g), 2))
    return t
    