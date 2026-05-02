import matplotlib.pyplot as plt

class Visualizer:
    def plot_signal(self, time, signal, title="Signal"):
        plt.figure()
        plt.plot(time, signal)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()