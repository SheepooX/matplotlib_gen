#!/usr/bin/env python

from simplifier import *
import numpy as np

sim = Simplifier()

x = np.arange(0, 6 * np.pi + 0.001 , 0.001)
f1 = 2
f2 = 7
f3 = 5
si = np.sin(2*np.pi*x/f1) + np.sin(2*np.pi*x/f2) + np.sin(2*np.pi*x/f3)

sim.plot(x, si)

sim.scale_axes()
sim.save_fig()

