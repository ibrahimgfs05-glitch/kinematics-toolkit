from simulations.kinematics import constant_velocity
from visualization.plotting import plot_motion

def run():
    x0 = 0
    v = 3.5
    t_max = 10
    dt = 0.1

    t, x = constant_velocity(x0, v, t_max, dt)

    plot_motion(t, x)

if __name__ == "__main__":
    run() 
