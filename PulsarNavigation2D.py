import random
import math
import numpy as np
import matplotlib.pyplot as plt


class Bounds:
    lo = -1000
    hi = 1000

    def set_bounds(self, low, high):
        self.lo = low
        self.hi = high


class Ship(Bounds):

    x = 0
    y = 0

    def generate_coordinates(self):
        self.x = random.uniform(self.lo, self.hi)
        self.y = random.uniform(self.lo, self.hi)


class Pulsar(Bounds):

    x_c = 0
    y_c = 0
    T = 100

    def __init__(self, xi, yi, T_o):
        self.x_c = xi
        self.y_c = yi
        self.T = T_o

    def spin(self, t):
        plt.ion()
        for i in range(t):
            func = lambda x: (x - self.x_c)*math.tan(2 * np.pi * i / self.T) + self.y_c
            y = np.array(range(self.lo, self.hi))
            x = func(y)
            plt.plot(x, y)
            plt.xlim([-1, 1])
            plt.ylim([-1, 1])
            plt.pause(0.00005)
            plt.cla()
        while True:
            plt.pause(0.00005)


