import numpy as np

def constant_velocity(parameters):
    t = parameters.t
    x = parameters.x0

    T = []
    X = []

    while t <= parameters.t_max:
        T.append(t)
        X.append(x)

        t = t + parameters.dt
        x = x + parameters.v0*parameters.dt
        

    return T, X

def constant_acceleration(parameters):
    t = parameters.t
    x = parameters.x0
    v = parameters.v0

    T = []
    X = []
    V = []

    while t <= parameters.t_max:
        T.append(t)
        V.append(v)
        X.append(x)

        t = t + parameters.dt
        v = v + parameters.a*parameters.dt
        x = x + v*parameters.dt
   

    return T, V, X