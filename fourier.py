#!/usr/bin/env python

from simplifier import *
import numpy as np

sim = Simplifier()

step = 0.01

freqs = [2, 3, 5, 7, 11, 13, 17]
freqs = [4]

x = np.arange(0, 20 * np.pi + step, step)
snd = np.sin(2 * np.pi * freqs[0] * x)
for f in freqs[1:]:
    snd = snd + np.sin(2 * np.pi * f * x)

fqs = np.arange(0, 20, 0.01)
fyr = []
fyi = []

for fq in fqs:
    omg = 2 * np.pi * fq
    shape = snd * (np.cos(omg * x) + 1j * np.sin(omg * x))
    x_avg = sum(shape.real) / len(shape.real)
    y_avg = sum(shape.imag) / len(shape.imag)
    fyr.append(x_avg)
    fyi.append(y_avg)

sim.plot(fqs, fyr, {'label': 'real', 'linewidth': 1})
sim.plot(fqs, fyi, {'label': 'imag', 'linewidth': 1})

sim.show_labels()
sim.save_fig()

