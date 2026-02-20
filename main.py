from simulations.kinematics import constant_velocity
from simulations.kinematics import constant_acceleration
from visualization.plotting import plot_motion_constant_velocity
from visualization.plotting import plot_motion_constant_acceleration
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

        

def run_all():
    print("running constant velocity")
    run_constant_velocity()
    print("\nrunning constant acceleration")
    run_constant_acceleration()



if __name__ == "__main__":
    print("Which simulation would you like to run?")
    print("1 : Constant velocity")
    print("2 : Constant acceleration")
    print("3 : Both")

    choice = input("Enter choice 1/2/3 :")

    if choice == "1":
        run_constant_velocity()
    elif choice == "2":
        run_constant_acceleration()
    elif choice == "3" :
        run_all()
    else :
        print("Invalid choice")
