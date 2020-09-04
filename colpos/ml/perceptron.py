import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Perceptron(object):

    def __init__(self, eta=0.5, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        # np.random.shuffle(X)
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.0, size=1 + X.shape[1])
        self.errors_ = []
        i = 0
        for i in range(self.n_iter):
            errors = 0
            j = 0
            print(f"EPOCH {i+1}:")
            for xi, target in zip(X, y):
                j += 1
                out = self.predict(xi), self.net_input(xi)
                update = self.eta * (target - out[0])
                self.w_[1:] += update * xi
                self.w_[0] += update
                print(f'\tout: {out}, w: {self.w_}')
                errors += int(update != 0.0)
            self.errors_.append(errors)
            i += 1
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


# AND
X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([1, -1, -1, -1])
ppn = Perceptron(eta=0.5, n_iter=8, random_state=3)
ppn.fit(X, y)
print("AND")
print(ppn.predict([1, 1]))
print(ppn.predict([0, 1]))
print(ppn.predict([1, 0]))
print(ppn.predict([0, 0]))
