import matplotlib.pyplot as plt

def plot_motion_constant_velocity(T, X):
    plt.plot(T, X)
    plt.title("Constant Velocity Graph")
    plt.xlabel("Time [s]")
    plt.ylabel("position [m]")
    plt.grid(True)
    plt.show()

def plot_motion_constant_acceleration(T, V, X):
    plt.subplot(1, 2, 1)
    plt.plot(T, X, "r")
    plt.title("Pos V time")
    plt.xlabel("time [s]")
    plt.ylabel("pos [m]")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(T, V, "g")
    plt.title("Vel V time")
    plt.xlabel("time [s]")
    plt.ylabel("vel [ms^-1]")
    plt.grid(True)

    plt.suptitle("Constant Acceleration Graphs")
    plt.tight_layout()
    plt.show()

def plot_projectile(results, name):

    #results = [time, x points, y points]


    plt.subplot(1, 3, 1)
    plt.plot(results[0], results[1], "g")
    plt.title("Time V X-pos")
    plt.xlabel("Time [s]")
    plt.ylabel("X-pos [m]")
    plt.grid(True)

    plt.subplot(1, 3, 2)
    plt.plot(results[0], results[2],"b")
    plt.title("Time V Y-pos")
    plt.xlabel("Time [s]")
    plt.ylabel("Y-pos [m]")
    plt.grid(True)
    
    plt.subplot(1, 3, 3)
    plt.plot(results[1], results[2], "r")
    plt.title("X-pos V Y-pos")
    plt.xlabel("X-Pos")
    plt.ylabel("Y-pos")
    plt.grid(True)


    if name == "drag":
        plt.suptitle("Projectile with drag")
    elif name == "no_drag":
        plt.suptitle("Projectile with no drag")

    plt.tight_layout()
    plt.show()
