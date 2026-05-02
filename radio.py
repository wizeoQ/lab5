import matplotlib.pyplot as plt
import numpy as np


# Генерация сигнала
class SignalGenerator:
    def __init__(self, frequancy, amplitude = 1.0):
        self.frequancy = frequancy
        self.amplitude = amplitude

        
    def generate(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequancy * time)

# Модуляция сигнала
class Modulator:
    def __init__(self, carrier_frequancy):
        self.carrier_frequancy = carrier_frequancy
    
    
    def am_modulate(self, signal, time):
        carrier = np.sin(2 * np.pi * self.carrier_frequancy * time)
        return (1 + signal) * carrier
    
    
    def fm_modulate(self, signal, time, modulation_index=1.0):
        phase = 2 * np.pi * self.carrier_frequancy * time + modulation_index * signal
        return np.sin(phase)


    def add_noise(self, signal, noise_level=0.1):
        noise = np.random.normal(0, noise_level, len(signal))
        return signal+noise
# Вывод графика
class Visualizer:
    def plot_signal(self, time, signal, title="Signal"):
        plt.figure()
        plt.plot(time, signal)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()


    def save_plot(self, time, signal, filename="signal.png"):
        plt.plot(time, signal)
        plt.savefig(filename)
        plt.close()

#=======================================================================        
time = np.linspace(0,1,1000)
signal_freq = 5 # Частота сигнала
carrier_freq = 50 # Частота несущей

# Генерация сигнала
generator = SignalGenerator(signal_freq)
signal = generator.generate(time)

# Модуляция
modulator = Modulator(carrier_freq)
am_signal = modulator.am_modulate(signal, time)
am_signal = modulator.add_noise(am_signal)
fm_signal = modulator.fm_modulate(signal, time)

# Визуализация
vizualizer = Visualizer()
vizualizer.plot_signal(time, signal, "Original Signal")
vizualizer.plot_signal(time, am_signal, "AM Signal")
vizualizer.plot_signal(time, fm_signal, "FM Signal")