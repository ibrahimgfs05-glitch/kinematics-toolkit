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

def plot_projectile_no_drag(T, x, y, vx, vy):
    plt.subplot(2, 3, 1)
    plt.plot(T, x, "g")
    plt.title("Time V X-pos")
    plt.xlabel("Time [s]")
    plt.ylabel("X-pos [m]")
    plt.grid(True)
    
    plt.subplot(2, 3, 2)
    plt.plot(T, y, "r")
    plt.title("Time V Y-pos")
    plt.xlabel("Time [s]")
    plt.ylabel("Y-pos [m]")
    plt.grid(True)

    plt.subplot(2, 3, 3)
    plt.plot(x, y, "b")
    plt.title("X-pos V Y-pos")
    plt.xlabel("X-Pos")
    plt.ylabel("Y-pos")
    plt.grid(True)

    plt.subplot(2, 3, 4)
    plt.plot(T, vy, "cyan")
    plt.title("Time V Vertical Vel")
    plt.xlabel("Time [s]")
    plt.ylabel("Vel [ms^-1]")
    plt.grid(True)

    plt.subplot(2, 3, 5)
    plt.plot(T, vx, "brown")
    plt.title("Time vs Horizontal Vel")
    plt.xlabel("Time [s]")
    plt.ylabel("Vel [ms^-1]")
    plt.grid(True)


    plt.suptitle("Projectile motion")
    plt.tight_layout()
    plt.show()
