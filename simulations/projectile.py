import numpy as np
import math

def projectile_no_drag(pos, theta, v0, a, t, dt):

    v = np.array([v0*math.sin(theta), v0*math.cos(theta)])
    T = []
    x = []
    y = []
    vx = []
    vy = []

    while pos[1] >= 0:
        T.append(t)
        x.append(pos[0])
        y.append(pos[1])
        vx.append(v[0])
        vy.append(v[1])

        t += dt
        pos = pos + v*dt
        v = v + a*dt
        
    return T, x, y, vx, vy