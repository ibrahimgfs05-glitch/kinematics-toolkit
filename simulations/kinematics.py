import numpy as np

def constant_velocity(x0, v, t_max, dt):
    t = np.arange(0,t_max, dt)
    x = x0 + v*t

    return t, x

def constant_acceleration(x0, v0, t_max, dt, a):
    t = np.arange(0, t_max, dt)
    v = v0 + a*t
    x = x0 + v*t + 1/2*a*t**2

    return t, x, v