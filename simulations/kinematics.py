import numpy as np

def constant_velocity(x0, v, t_max, dt):
    t = np.arange(0,t_max, dt)
    x = x0 + v*t

    return t, x