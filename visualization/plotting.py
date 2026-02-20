import matplotlib.pyplot as plt

def plot_motion_constant_velocity(t, x):
    plt.plot(t, x)
    plt.title("Constant Velocity Graphs")
    plt.xlabel("Time [s]")
    plt.ylabel("position [m]")
    plt.grid(True)
    plt.show()

def plot_motion_constant_acceleration(t, x, v):
    plt.subplot(1, 2, 1)
    plt.plot(t, x, "r")
    plt.title("Pos V time")
    plt.xlabel("time [s]")
    plt.ylabel("pos [m]")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(t, v, "g")
    plt.title("Vel V time")
    plt.xlabel("time [s]")
    plt.ylabel("vel [ms^-1]")
    plt.grid(True)

    plt.suptitle("Constant Acceleration Graphs")
    plt.tight_layout()
    plt.show()
