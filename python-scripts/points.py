#!/usr/bin/env python3
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm


def set_direction():
    while True:
        x = randint(-1, 1)
        y = randint(-1, 1)
        if x != 0 or y != 0:
            break
    return x, y


class Point:
    def __init__(self, x, y, m, color):
        self.x = x
        self.y = y
        self.n = 0
        self.m = m
        self.color = color
        self.dir_x, self.dir_y = set_direction()
        self.array = [[self.x], [self.y], [self.color]]

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
        if self.n >= self.m:
            self.array[2].append("blue")
        else:
            self.array[2].append(self.color)
        return self

    def move_n(self, n):
        for _ in range(0, n):
            self.move()
        return self

    def __str__(self):
        return f"Point({self.x},{self.y}) #{self.n}"


sim = []
for i in enumerate(range(10)):
    p = Point(randint(-5, 5), randint(-2, 2), i[0] * 3, (5 * ["red", "green"])[i[0]],)
    s = p.move_n(30).array
    sim.append(s)

data = np.array(sim)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(-6, 6)
plt.ylim(-3, 3)
plt.tick_params(
    axis="both",
    which="both",
    bottom=False,
    top=False,
    labelbottom=False,
    right=False,
    left=False,
    labelleft=False,
)
ims = []
for i, num in enumerate(range(0, 30)):
    x, y, c = [], [], []
    for point in data[:, :3, num]:
        x.append(int(point[0]))
        y.append(int(point[1]))
        c.append(point[2])
    print(i, x, y, c)
    scat = ax.scatter(x=x, y=y, s=50, c=c)
    ims.append([scat])

im_ani = animation.ArtistAnimation(fig, ims, interval=800, repeat_delay=300, blit=True)
plt.show()
