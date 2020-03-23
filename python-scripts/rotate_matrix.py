#!/usr/bin/env python3
import numpy as np

abc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(np.matrix(abc))

# counterclockwise
# Reverse rows an then transpose the matrix
print("\nRotate counterclockwise:")
print(np.matrix([list(r) for r in zip(*[list(reversed(r)) for r in abc])]))


# clockwise
# Transpose matrix and then reverse rows
print("\nRotate clockwise:")
rotate_cw = [list(r) for r in zip(*reversed(abc))]
print(np.matrix(rotate_cw))
print()
rotate_cw = [list(reversed(r)) for r in zip(*abc)]
print(np.matrix(rotate_cw))
