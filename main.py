from simulations.kinematics import constant_velocity
from simulations.kinematics import constant_acceleration
from simulations.projectile import projectile
from visualization.plotting import plot_motion_constant_velocity
from visualization.plotting import plot_motion_constant_acceleration
from visualization.plotting import plot_projectile
from Configs.projectile_configs import no_drag_params
import math
import numpy as np

def run_constant_acceleration():
    x0 = 0
    t_max = 10
    dt = 0.01
    v0 = 350
    a = -9.8
    t, x, v = constant_acceleration(x0, v0, t_max, dt, a)
    plot_motion_constant_acceleration(t, x, v)


def run_constant_velocity():
    x0 = 0
    t_max = 115
    dt = 0.01
    v = 3.5
    t, x = constant_velocity(x0 , v, t_max, dt)
    np.full_like(t,v)
    plot_motion_constant_velocity(t, x)

def run_projectile_no_drag():
    parameters = no_drag_params(35, 60)     #no_drag_params(v0, theta, pos(if none : (0,0)))
    T, x, y, vx, vy = projectile(parameters)
    plot_projectile(T, x, y, vx, vy)

def run_projectile_drag():
    
    params = {
        "Cd" : 0.47,
        "rho" : 1.225,
        "A" : 0.5,
        "pos" : np.array([0,0]),
        "v0" :  35,
        "theta" : math.degrees(45),
        "g" : np.array([0, -9.8]),
        "t" : 0,
        "dt" : 0.01,
        "name" : "no_drag",
        "k" : 0.5*params.Cd*params.rho*params.A
    }

    T, x, y, vx, vy = projectile(params)
    plot_projectile(T, x, y, vx, vy)



        

def run_all():
    print("running constant velocity")
    run_constant_velocity()
    print("\nrunning constant acceleration")
    run_constant_acceleration()
    print("\nRunning projectile motion with no drag")
    run_projectile_no_drag()
    print("\nRunning projectile motion with drag")



if __name__ == "__main__":
    print("Which simulation would you like to run?")
    print("1 : Constant velocity")
    print("2 : Constant acceleration")
    print("3 : Projectile with no drag")
    print("4 : All")

    choice = input("Enter choice 1/2/3/4 :")

    if choice == "1":
        run_constant_velocity()
    elif choice == "2":
        run_constant_acceleration()
    elif choice == "3":
        run_projectile_no_drag()
    elif choice == "4" :
        run_all()
    else :
        print("Invalid choice")
