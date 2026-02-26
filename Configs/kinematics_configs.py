import numpy as np

class constant_velocity:
    def __init__(self, x0, v0, t, t_max, dt):
        self.x0 = x0
        self.v0 = v0
        self.t = t
        self.t_max = t_max
        self.dt = dt

class constant_acceleration:
    def __init__(self, x0, v0, t, t_max, dt, a, initial_pos):
        self.x0 = x0
        self.v0 = v0
        if initial_pos == None:
            self.initial_pos = np.array([0,0])
        else:
            self.initial_pos = np.array(initial_pos)
        self.a = a
        self.t = t
        self.t_max = t_max
        self.dt = dt