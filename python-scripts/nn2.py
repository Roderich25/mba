import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()
X, y = spiral_data(100, 3)

# print(X)
# print(y)


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLu:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer1 = Layer_Dense(2, 50)
activation1 = Activation_ReLu()

layer1.forward(X)
# print(layer1.output)
# print(layer1.output.shape)

activation1.forward(layer1.output)
print(activation1.output)
print(activation1.output.shape)
