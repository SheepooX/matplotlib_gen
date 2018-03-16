#!/usr/bin/env python

from d2 import *
import numpy as np
import math

step = 0.01

func = [
        [
            (lambda x: 1, 'O(1)'),
            (lambda x: x, 'O(n)'),
            (lambda x: math.log(x), 'O(log n)'),
            (lambda x: math.sqrt(x), 'O(sqrt(n))'),
        ], [
            (lambda x: x * math.log(x), 'O(n * log n)'),
            (lambda x: x ** 3, 'O(n**3)'),
            (lambda x: 2 ** x, 'O(2 ** n)'),
            (lambda x: math.factorial(int(x)), 'O(n!)')
            ],
        ]

sim = Simplifier(rows=2, cols=4, width=28, height=21)

lim = 10
x = np.arange(1 + step, lim, step)
x1 = [0, lim]
y1 = [0, 0]
x2 = [0, 0]
y2 = [0, lim]

for i in range(2):
    for j in range(4):
        y = [func[i][j][0](x1) for x1 in x]
        sim.plot(x, y, row=i, col=j, opts={'label': func[i][j][1]})
        sim.plot(x1, y1, row=i, col=j, opts={'color': 'w'})
        sim.plot(x2, y2, row=i, col=j, opts={'color': 'w'})

for axis in sim.axes[0]:
    axis.axis('equal')

for axis in sim.axes[1][:1]:
    axis.axis('equal')

sim.show_labels()
sim.save_fig()

