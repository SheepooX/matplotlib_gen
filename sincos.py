#!/usr/bin/env python

import d2
import numpy as np

d2.init()

x = np.arange(0, 6 * np.pi + 0.001 , 0.001)
peri = 2 * np.pi
si = np.e ** (2 * np.pi * 1j * x * (1 / peri))

d2.plot(si.real, si.imag, opts={'label': 'circle'})
d2.plot(x, si.real, opts={'label': 'cos x'})
d2.plot(x, si.imag, opts={'label': 'sin  x'})

d2.axis_scale()
d2.finish()

