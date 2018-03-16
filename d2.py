#!/usr/bin/env python

import sys
import matplotlib as mpl
import numpy as np
import random
import lorem

mpl.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon


fig = None
ax = None

def init(rows=1, cols=1, width=8, height=8):
    global ax, fig
    fig = plt.figure(figsize=(width, height))
    index = (a + 1 for a in range(rows * cols))
    ax = [[fig.add_subplot(rows, cols, next(index)) for j in range(cols)] for i in range(rows)]


def plot(x, y, row=0, col=0, opts={}):
    return ax[row][col].plot(x, y, **opts)

def patch(poly, row=0, col=0, opts={}):
    return ax[row][col].add_patch(poly)

def get_graph(a, b, f):
    x = np.linspace(a, b)
    y = [f(w) for w in x]
    return x, y

def get_integral(a, b, f, opts={'facecolor': '0.4', 'alpha': 0.5}):
    x, y = get_graph(a, b, f)
    verts = [(a, 0)] + list(zip(x, y)) + [(b, 0)]
    return Polygon(verts, **opts)

def graph(a, b, f, opts={}, row=0, col=0):
    x, y = get_graph(a, b, f)
    return plot(x, y, row, col, opts)

def graph_integral(a, b, f, opts1={}, opts2={}, row=0, col=0):
    poly = get_integral(a, b, f, opts1)
    return patch(poly, row, col, opts2)

def setup_labels():
    for row in ax:
        for a in row:
            handles, labels = a.get_legend_handles_labels()
            a.legend(handles, labels)

def iterate_axis(func):
    for row in ax:
        for axis in row:
            func(axis)

def scale_axis(scale='equal'):
    iterate_axis(lambda axis: axis.axis(scale))

def clear_axis():
    iterate_axis(lambda axis: axis.clear())

fig_dir = "./figs"
tmp_file = "{}/_last".format(fig_dir)

def save_fig(name=None, tmp=True):
    with open("next_number", mode="r") as fi:
        s = fi.readline()[:-1]
        num = int(s)
    with open("next_number", mode="w") as fi:
        fi.write("{}\n".format(num + 1))
    if name is None:
        name = "{:05d}_{}".format(num, "".join(random.sample(lorem.lorem, 2)))
    else:
        name = "{:05d}_{}".format(num, name)
    plt.savefig("{}/{}.png".format(fig_dir, name), dpi=200)
    plt.savefig("{}.png".format(tmp_file), dpi=200)
    print(name)


def finish(name=None):
    setup_labels()
    save_fig(name)


if __name__ == '__main__':
    fx = lambda x: (x - 2) ** 2 - 10
    init(width=6, height=4)
    graph(0, 8, fx, {'label': '(x - 2) ** 2 - 10'})
    graph_integral(2, 7, fx, {'facecolor': 'blue', 'edgecolor': 'red', 'alpha': 0.3}, {})
    finish('_test')

