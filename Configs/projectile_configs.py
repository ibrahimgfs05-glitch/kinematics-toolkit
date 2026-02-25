import numpy as np
import math

class no_drag_params:
    def __init__(self ,name , v0, theta, initial_pos = None):
        self.name = name
        self.v0 = v0 
        if initial_pos == None:
            self.pos = np.array([0,0])
        else :
            self.pos = np.array(initial_pos)
        self.theta = math.radians(theta)
        self.g = np.array([0, -9.8])
        self.t = 0
        self.dt = 0.01

class drag_params:
    def __init__(self ,name ,v0 , theta, Cd, rho, A, initial_pos=None):
        self.name = name
        self.Cd = Cd
        self.rho = rho
        self.A = A
        self.v0 = v0
        if initial_pos == None:
            self.pos = np.array([0, 0])
        else :
            self.pos = np.array([initial_pos])
        self.theta = math.radians(theta)
        self.g = np.array([0, -9.8])
        self.t = 0
        self.dt = 0.01

    