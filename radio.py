import numpy as np


# 5.4 - разработать проект симулятор радиоканала
# 5.1 - создать классы для генерации сигналов и их модуляци
# 5.4.1.1 Класс SignalGenerator
class SignalGenerator:
    def __init__(self, frequancy, amplitude = 1.0):
        self.frequancy = frequancy
        self.amplitude = amplitude
        
    def genetate(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequancy * time)

# 5.4.1.2 Класс Modulator
class Modulator:
    def __init__(self, carrier_frequancy):
        self.carrier_frequancy = carrier_frequancy
    
    def am_modulate(self, signal, time):
        carrier = np.sin(2 * np.pi * self.carrier_frequancy * time)
