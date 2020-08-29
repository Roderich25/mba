import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        # np.random.shuffle(X)
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []
        i = 0
        for _ in range(self.n_iter):
            errors = 0
            j = 0
            for xi, target in zip(X, y):
                j += 1
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                if update != 0:
                    # print(f"Rodrigo {i}:{j}:", self.w_, update*xi, update, xi)
                    pass
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
            i += 1
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


df = pd.read_csv('iris.data', header=None, encoding='utf-8')
#df = df.sample(frac=1)
print(df.tail())
###


# select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values


# ### Training the perceptron model


ppn = Perceptron(eta=0.1, n_iter=40, random_state=3)

ppn.fit(X, y)
print(ppn.w_)
print(ppn.errors_)

# plot data
plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='versicolor')

plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

plt.show()

plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')

plt.show()
