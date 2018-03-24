#!/usr/bin/env python

from simplifier import *
import numpy as np

sim = Simplifier(width=10, height=4)

x = np.arange(0, 6 * np.pi + 0.001 , 0.001)
peri = 2 * np.pi
si = np.e ** (2 * np.pi * 1j * x * (1 / peri))

sim.plot(si.real, si.imag, opts={'label': 'circle'})
sim.plot(x, si.real, opts={'label': 'cos x'})
sim.plot(x, si.imag, opts={'label': 'sin  x'})

sim.scale_axes()
sim.save_fig()

