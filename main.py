from simulations.kinematics import constant_velocity
from simulations.kinematics import constant_acceleration
from simulations.projectile import projectile
from visualization.plotting import plot_motion_constant_velocity
from visualization.plotting import plot_motion_constant_acceleration
from visualization.plotting import plot_projectile
from Configs.projectile_configs import no_drag_params
from Configs.projectile_configs import drag_params
from Configs.kinematics_configs import constant_velocity
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
    parameters = constant_velocity(0, 35, 0, 15, 1) #constant_velocity(x0, v0, t, t_max, dt)
    t, x = constant_velocity(parameters)
    plot_motion_constant_velocity(t, x)

def run_projectile_no_drag():
    parameters = no_drag_params("no_drag", 35, 60) #no_drag_params(name, v0, theta, initial_pos(if none(0,0)))
    T, x, y, vx, vy, name = projectile(parameters)
    plot_projectile(T, x, y, vx, vy, name)

def run_projectile_drag():
    
    parameters = drag_params("drag", 35, 60, 0.47, 1.225, 0.5) #no_drag_params(name, v0, theta, Cd, rho, A, initial_pos(if none(0,0)))
    T, x, y, vx, vy, name = projectile(parameters)
    plot_projectile(T, x, y, vx, vy, name)



        

def run_all():
    print("running constant velocity")
    run_constant_velocity()
    print("\nrunning constant acceleration")
    run_constant_acceleration()
    print("\nRunning projectile motion with no drag")
    run_projectile_no_drag()
    print("\nRunning projectile motion with drag")
    run_projectile_drag()



if __name__ == "__main__":
    print("Which simulation would you like to run?")
    print("1 : Constant velocity")
    print("2 : Constant acceleration")
    print("3 : Projectile with no drag")
    print("4 : Projectile with drag")
    print("5 : All")

    choice = input("Enter choice 1/2/3/4/5 :")

    if choice == "1":
        run_constant_velocity()
    elif choice == "2":
        run_constant_acceleration()
    elif choice == "3":
        run_projectile_no_drag()
    elif choice == "4":
        run_projectile_drag()
    elif choice == "5" :
        run_all()
    else :
        print("Invalid choice")
