import numpy as np
import math



def projectile(parameters):
    #params(name, v0, theta_type(dynamic or fixed), theta, initial_pos(if None = (0,0)
    results = [[] , [] , []]  #[time, x points, y points, vx, vy]

    def name():
        return parameters.name
    name = name()

    if parameters.theta_type == "dynamic":
        for i in range(15, 105, 15):
            parameters.theta = math.radians(i)
            theta = parameters.theta

            v = np.array([parameters.v0*math.cos(theta), parameters.v0*math.sin(theta)])
            pos = parameters.pos.copy()
            t = parameters.t
            speed = np.linalg.norm(v)

            T = []
            x = []
            y = []
            
            while pos[1] >= 0:

                T.append(t)
                x.append(pos[0])
                y.append(pos[1])

                if name == "drag": 
                    t = t + parameters.dt
                    a = parameters.g - 0.5*parameters.Cd*parameters.rho*parameters.A*v*speed
                    v = v + a*parameters.dt
                    pos = pos + v*parameters.dt
                    speed = np.linalg.norm(v)

                elif name == "no_drag":
                    t = t + parameters.dt  
                    v = v + parameters.g*parameters.dt
                    pos = pos + v*parameters.dt

            results[0].extend(T)
            results[1].extend(x)
            results[2].extend(y)

            results[0].append(None)
            results[1].append(None)
            results[2].append(None)

            if i == 90:
                 return results, name    
                    
           
    elif parameters.theta_type == "fixed":
        theta = parameters.theta

        v = np.array([parameters.v0*math.cos(theta), parameters.v0*math.sin(theta)])
        pos = parameters.pos.copy()
        t = parameters.t
        speed = np.linalg.norm(v)

        T = []
        x = []
        y = []
            
        while pos[1] >= 0:

            T.append(t)
            x.append(pos[0])
            y.append(pos[1])

            if name == "drag": 
                t = t + parameters.dt
                a = parameters.g - 0.5*parameters.Cd*parameters.rho*parameters.A*v*speed
                v = v + a*parameters.dt
                pos = pos + v*parameters.dt
                speed = np.linalg.norm(v)

            elif name == "no_drag":
                t = t + parameters.dt  
                v = v + parameters.g*parameters.dt
                pos = pos + v*parameters.dt

        results[0].extend(T)
        results[1].extend(x)
        results[2].extend(y)

        return results, name    
            
    
    






