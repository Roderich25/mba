#!/usr/bin/env python3
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def set_direction():
    while True:
        x = randint(-1, 1)
        y = randint(-1, 1)
        if x != 0 or y != 0:
            break
    return x, y


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = 0
        self.dir_x, self.dir_y = set_direction()
        self.array = [[self.x], [self.y]]

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y
        self.n += 1
        if self.x == 6 or self.x == -6:
            self.dir_x = self.dir_x * -1
        if self.y == 3 or self.y == -3:
            self.dir_y = self.dir_y * -1
        self.array[0].append(self.x)
        self.array[1].append(self.y)
        print(self)
        return self

    def move_n(self, n):
        for _ in range(0, n):
            self.move()
        return self

    def __str__(self):
        return f"Point({self.x},{self.y}) #{self.n}"


a = Point(0, 0)
sim = a.move_n(25).array


def update_line(num, data, line):
    line.set_data(data[..., num])
    return (line,)


fig = plt.figure()

data = np.array(sim)
(l,) = plt.plot([], [], ". r")
plt.xlim(-6, 6)
plt.ylim(-3, 3)
line_ani = animation.FuncAnimation(
    fig, update_line, 25, fargs=(data, l), interval=500, blit=True
)
plt.show()
