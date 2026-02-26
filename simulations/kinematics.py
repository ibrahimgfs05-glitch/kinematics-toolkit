import numpy as np

def constant_velocity(parameters):
    t = parameters.t
    x = parameters.x0

    while t <= parameters.t_max:
        t = np.arange(parameters.t , parameters.t_max, parameters.dt)
        x = x + parameters.v0*parameters.dt

    return t, x

def constant_acceleration(parameters):
    t = np.arange(0, parameters.t_max, parameters.dt)
    v = parameters.v + a*dt
    x = x0 + v*dt

    return t, x, v