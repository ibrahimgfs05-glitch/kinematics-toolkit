import numpy as np
import math

class no_drag_params:
        def __init__(self, v0= 35, theta= 60, pos = None):
            self.name = "no_drag"
            self.v0 = v0 
            if pos == None:
                self.pos = np.array([0,0])
            else :
                self.pos = np.array(pos)
            self.theta = math.radians(60)
            self.g = np.array([0, -9.8])
            self.t = 0
            self.dt = 0.01

def get_drag_params():
    return {
        "name" : "no drag",
        "Cd" : 0.47,
        "rho" : 1.225,
        "A" : 0.5, 
        "k" : 0.5,
        "v0" : 35,
        "pos" : np.array([0, 0]),
        "theta" : math.radians(60),
        "g" : np.array([0, -9.8]),
        "t" : 0,
        "dt" : 0.01,

    }

    