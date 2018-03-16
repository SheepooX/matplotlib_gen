#!/usr/bin/env python

from simplifier import *
import numpy as np

sim = Simplifier()

step = 0.01

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377
freqs = [np.pi]
wfs = [(377 + 233) / 377]

fq_str = ','.join([str(f) for f in freqs])

x = np.arange(0, 30 + step, step)
snd = np.sin(2 * np.pi * freqs[0] * x)
for f in freqs[1:]:
    ome = 2 * np.pi * f
    snd = snd + np.sin(ome * x)

for wf in wfs:
    ome = 2 * np.pi * wf
    shape = snd * (np.cos(ome * x) + 1j * np.sin(ome * x))
    sim.clear_axes()
    lbl = "f:{};wf:{}".format(fq_str, wf)
    sim.plot(shape.real, shape.imag, {'label': lbl, 'linewidth': 1})
    sim.scale_axes()
    sim.show_labels()
    sim.save_fig("f:{},wf:{}".format(fq_str, wf))


