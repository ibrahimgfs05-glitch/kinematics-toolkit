import numpy as np
import math


def projectile(parameters):

    pos = parameters.pos.copy()
    t = parameters.t
    v = np.array([parameters.v0*math.cos(parameters.theta), parameters.v0*math.sin(parameters.theta)])
    speed = np.linalg.norm(v)
    T = []
    x = []
    y = []
    vx = []
    vy = []

    def name():
        return parameters.name
    name = name()

    while pos[1] >= 0:

        T.append(t)
        x.append(pos[0])
        y.append(pos[1])
        vx.append(v[0])
        vy.append(v[1])

        if name == "drag": 
            t = t + parameters.dt
            a = parameters.g - 0.5*parameters.Cd*parameters.rho*parameters.A*v*speed
            v = v + a*parameters.dt
            pos = pos + v*parameters.dt
            speed = np.linalg.norm(v)

        elif name == "no_drag":
            t = t + parameters.dt  
            pos = pos + v*parameters.dt
            v = v + parameters.g*parameters.dt
        
    return T, x, y, vx, vy, name