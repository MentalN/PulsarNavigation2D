import random


class Ship:

    x = 0
    y = 0

    def generate_coordinates(self):
        self.x = random.uniform(-1500, 1500)
        self.y = random.uniform(-1500, 1500)


class Pulsar:

    x_coords = []
    y_coords = []
    verf_num = 0

    def generate(self):
        numPulsars = int(input("Number of pulsars > "))
        self.verf_num = numPulsars
        for it in range(numPulsars+1):
            self.x_coords.append(random.uniform(-1500, 1500))
            self.y_coords.append(random.uniform(-1500, 1500))


