import matplotlib.pyplot as plt

def plot_motion(t, x):
    plt.plot(t, x)
    plt.title("Kinematics")
    plt.xlabel("Time [s]")
    plt.ylabel("position [m]")
    plt.grid(True)
    plt.show()
