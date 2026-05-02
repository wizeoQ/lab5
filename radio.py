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

# 5.4.2. Расширение функционала классов:
# 5.4.2.1. Добавление других видов модуляции
    def fm_modulate(self, signal, time, modulation_index=1.0):
        phase = 2 * np.pi * self.carrier_frequancy * time + modulation_index * signal
        return np.sin(phase)
    
# 5.4.2.3 Добавление шума
    def add_noise(self, signal, noise_level=0.1):
        noise = np.random.normal(0, noise_level, len(signal))
        return signal+noise