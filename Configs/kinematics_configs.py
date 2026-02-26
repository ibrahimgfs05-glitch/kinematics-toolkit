import numpy as np

class constant_velocity_params:
    def __init__(self, t, v0, x0, t_max, dt):
        self.name = "constant velocity"
        self.x0 = x0
        self.v0 = v0
        self.t = t
        self.t_max = t_max
        self.dt = dt

class constant_acceleration_params:
    def __init__(self, x0, v0, t, t_max, dt, a):
        self.x0 = x0
        self.v0 = v0
        self.a = a
        self.t = t
        self.t_max = t_max
        self.dt = dt