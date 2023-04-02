from sympy import *
import numpy as np

x,y,w = symbols('x y w')


def signal_components(amplitude, min_frequency, max_frequency, wave_freqs_interval):
    waves = []
    for i in np.arange(min_frequency, max_frequency, wave_freqs_interval):
        waves.append([amplitude, round(i, 3)])

    return waves


waves = signal_components(1, 0.1, 1, 0.05)  # (amplitude of all sinusoids,    min frequency of sinusoid created,    max frequency of sinusoid created,    interval of created sinusoids' frequencies)
print(waves)


def signal(waves):
    signals = []
    signal = None

    for i in waves:
        wave = i[0] * sin(i[1] * 2*pi * x)
        signals.append(wave)

    for i in range(len(signals)):
        if i == 0:
            signal = signals[i]
        else:
            signal = signal + signals[i]

    return signal


signal = signal(waves)
plot(signal)

f = fourier_transform(signal, x, w)
print(f)
plot(f)