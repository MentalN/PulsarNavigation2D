import random
import math
import numpy as np
import matplotlib.pyplot as plt


class Space:
    VerfNum = 0
    lo = -1000
    hi = 1000

    def set_bounds(self, low, high):
        self.lo = low
        self.hi = high


class Ship(Space):

    x = 0
    y = 0

    def set_coordinates(self, xo, yo):
        self.x = xo
        self.y = yo

    def generate_coordinates(self):
        self.x = random.uniform(self.lo, self.hi)
        self.y = random.uniform(self.lo, self.hi)

    def verify_location(self, numPulsar, pulsar):
        self.uniques=[]

        for x in range(numPulsar):
            self.uniques.append(x)

        for i in range(numPulsar):
            for j in range(numPulsar):
                if i == j:
                    continue
                if pulsar[i].T == pulsar[j].T:
                    Space.VerfNum -= 1
                    self.uniques.remove(i)
                    self.unique.remove[j]
        return Space.VerfNum

    def angleTo(self, pulsar):
        return math.atan((pulsar.get_y() - self.y)/(pulsar.get_x()-self.x))

    def triangulate(self):



class Pulsar(Space):

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

    def get_period(self):
        return self.T

    def get_y(self):
        return self.y_c

    def get_x(self):
        return self.x_c


num_pulsars = int(input("Enter number of pulsars > "))
Space.VerfNum = num_pulsars
pulsars = [Pulsar(float(input("Pulsar x-coord > ")), float(input("y-coord > ")), float(input("Period > ")))
           for i in range(num_pulsars)]


