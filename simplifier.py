#!/usr/bin/env python

import sys
import matplotlib as mpl
import numpy as np
import random
import lorem

mpl.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

def get_graph(a, b, f):
    x = np.linspace(a, b)
    y = [f(w) for w in x]
    return x, y

def get_integral(a, b, f, opts={'facecolor': '0.4', 'alpha': 0.5}):
    x, y = get_graph(a, b, f)
    verts = [(a, 0)] + list(zip(x, y)) + [(b, 0)]
    return Polygon(verts, **opts)


class Simplifier:

    def __init__(self, rows=1, cols=1, width=8, height=8, fig_dir='./figs'):
        self.fig = plt.figure(figsize=(width, height))
        index = (a + 1 for a in range(rows * cols))
        self.axes = [[self.fig.add_subplot(rows, cols, next(index)) for j in range(cols)] for i in range(rows)]
        self.fig_dir = fig_dir
        self.tmp_file = "{}/_last".format(fig_dir)

    def plot(self, x, y, opts={}, row=0, col=0):
        return self.axes[row][col].plot(x, y, **opts)

    def plot_integral(self, poly, opts={}, row=0, col=0):
        return self.axes[row][col].add_patch(poly)

    def compute_and_plot(self, a, b, f, opts={}, row=0, col=0):
        x, y = get_graph(a, b, f)
        return self.plot(x, y, row, col, opts)

    def compute_and_plot_integral(self, a, b, f, opts1={}, opts2={}, row=0, col=0):
        poly = get_integral(a, b, f, opts1)
        return self.plot_integral(poly, row, col, opts2)

    def show_labels(self):
        for row in self.axes:
            for axis in row:
                handles, labels = axis.get_legend_handles_labels()
                axis.legend(handles, labels)

    def iterate_axes(self, func):
        for row in self.axes:
            for axis in row:
                func(axis)

    def scale_axes(self, scale='equal'):
        self.iterate_axes(lambda axis: axis.axis(scale))

    def clear_axes(self):
        self.iterate_axes(lambda axis: axis.clear())

    def save_fig(self, name=None, tmp=True):
        with open("next_number", mode="r") as fi:
            s = fi.readline()[:-1]
            num = int(s)
        with open("next_number", mode="w") as fi:
            fi.write("{}\n".format(num + 1))
        if name is None:
            name = "{:05d}_{}".format(num, "".join(random.sample(lorem.lorem, 2)))
        else:
            name = "{:05d}_{}".format(num, name)
        plt.savefig("{}/{}.png".format(self.fig_dir, name), dpi=200)
        plt.savefig("{}.png".format(self.tmp_file), dpi=200)
        return name


if __name__ == '__main__':
    simplif = Simplifier(width=6, height=4)
    fx = lambda x: (x - 2) ** 2 - 10
    simplif.compute_and_plot(0, 8, fx, {'label': '(x - 2) ** 2 - 10'})
    simplif.compute_and_plot_integral(2, 7, fx, {'facecolor': 'blue', 'edgecolor': 'red', 'alpha': 0.3}, {})
    simplif.show_labels()
    rtn = simplif.save_fig('_test')
    print(rtn)

