import numpy as np
import math

def projectile(parameters):
    
    v = np.array([parameters.v0*math.cos(parameters.theta), parameters.v0*math.sin(parameters.theta)])
    speed = np.linalg.norm(v)
    T = []
    x = []
    y = []
    vx = []
    vy = []
    
    while True:

        if parameters.name == "drag": 
            t = parameters.t + parameters.dt
            a = parameters.g - 0.5*parameters.Cd*parameters.rho*parameters.A*v*speed
            v = v + a*parameters.dt
            pos = parameters.pos + v*parameters.dt
            speed = np.linalg.norm(v)

        elif parameters.name == "no_drag":
            t = parameters.t + parameters.dt  
            pos = parameters.pos + v*parameters.dt
            v = v + parameters.g*parameters.dt
        
        T.append(t)
        x.append(pos[0])
        y.append(pos[1])
        vx.append(v[0])
        vy.append(v[1])

        if pos[1] == 0:
            break
        
    return T, x, y, vx, vy