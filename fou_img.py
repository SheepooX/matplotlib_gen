#!/usr/bin/env python

import d2
from matplotlib import pyplot as plt
import numpy as np

d2.init()

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
    d2.clear_axis()
    lbl = "f:{};wf:{}".format(fq_str, wf)
    d2.ax[0][0].plot(shape.real, shape.imag, label=lbl, linewidth=1)
    d2.scale_axis()
    d2.finish("f:{},wf:{}".format(fq_str, wf))


